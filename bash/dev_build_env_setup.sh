#!/bin/bash
set -e

# Updating linux repo list and setting non interactive terminal
sudo apt-get update

# Install postgresql client to use psql (postgresql alias)
sudo apt-get -y install --no-install-recommends postgresql-client

# Install minio for S3 file I/O
curl -O https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x mc
sudo mv ./mc /usr/bin

# Install python packages
source bash/dev_install_python_packages.sh
