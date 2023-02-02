#!/bin/bash
# A collection of utility functions used in build scripts

# Function to set Environmental Variables
function set_env {
  for envfile in $@; do
    if [ -f $envfile ]; then
      export $(cat $envfile | sed 's/#.*//g' | xargs)
    fi
  done
}

# Function to parse the database url
function urlparse {
  proto="$(echo $1 | grep :// | sed -e's,^\(.*://\).*,\1,g')"
  url=$(echo $1 | sed -e s,$proto,,g)
  userpass="$(echo $url | grep @ | cut -d@ -f1)"
  BUILD_PWD=$(echo $userpass | grep : | cut -d: -f2)
  BUILD_USER=$(echo $userpass | grep : | cut -d: -f1)
  hostport=$(echo $url | sed -e s,$userpass@,,g | cut -d/ -f1)
  BUILD_HOST="$(echo $hostport | sed -e 's,:.*,,g')"
  BUILD_PORT="$(echo $hostport | sed -e 's,^.*:,:,g' -e 's,.*:\([0-9]*\).*,\1,g' -e 's,[^0-9],,g')"
  BUILD_DB="$(echo $url | grep / | cut -d/ -f2-)"
}

# Function to get authorization levels for each dataset (public read vs private)
function get_acl {
  local name=$1
  local version=${2:-latest} #default version to latest
  local config_curl=$URL/datasets/$name/$version/config.json
  local statuscode=$(curl --write-out '%{http_code}' --silent --output /dev/null $config_curl)
  if [[ "$statuscode" -ne 200 ]]; then
    echo "private"
  else
    echo "public-read"
  fi
}

# Function to get version of dataset from Digital Ocean EDM Recipes
function get_version {
  local name=$1
  local version=${2:-latest} #default version to latest
  local acl=${3:-public-read}
  local config_curl=$URL/datasets/$name/$version/config.json
  local config_mc=spaces/edm-recipes/datasets/$name/$version/config.json
  if [ "$acl" != "public-read" ]; then
    local version=$(mc cat $config_mc | jq -r '.dataset.version')
  else
    local version=$(curl -sS $config_curl | jq -r '.dataset.version')
  fi
  echo "$version"
}

# Function to update a datset's version record
function record_version {
  local datasource="$1"
  local version="$2"
  psql $BUILD_ENGINE -q -c "
  DELETE FROM versions WHERE datasource = '$datasource';
  INSERT INTO versions VALUES ('$datasource', '$version');
  "
}

# Fucntion to check if the data has already been loaded into the database
function get_existence {
  local name=$1
  local version=${2:-latest} #default version to latest
  existence=$(psql $BUILD_ENGINE -t -c "
    SELECT EXISTS (
      SELECT FROM information_schema.tables 
      WHERE  table_schema = 'public'
      AND    table_name   = '$name'
    ) and EXISTS (
      SELECT FROM versions
      WHERE  datasource = '$name'
      AND    version   = '$version'
    );
  ")
  echo $existence
}

# Function to import data directly from Digital Ocean i.e. key function of dataloading
function import {
  local name=$1
  local version=${2:-latest} #default version to latest
  local acl=$(get_acl $name $version)
  local version=$(get_version $name $version $acl)
  local existence=$(get_existence $name $version)
  local target_dir=$(pwd)/.library/datasets/$name/$version
  # Download sql dump for the datasets from data library
  if [ -f $target_dir/$name.sql ]; then
    echo "✅ $name.sql exists in cache"
  else
    echo "🛠 $name.sql doesn't exists in cache, downloading ..."
    mkdir -p $target_dir && (
      cd $target_dir
      if [ "$acl" != "public-read" ]; then
        mc cp spaces/edm-recipes/datasets/$name/$version/$name.sql $name.sql
      else
        curl -O $URL/datasets/$name/$version/$name.sql $name.sql
      fi
    )
  fi
  # Loading into Database
  if [ "$existence" == "t" ]; then
    echo "NAME: $name VERSION: $version is already loaded in postgres!"
  else
    psql $BUILD_ENGINE -f $target_dir/$name.sql
  fi
  record_version "$name" "$version"
}
