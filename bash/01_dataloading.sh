#!/bin/bash
source bash/config.sh

# Run postgres with less output and create a table of versions by dataset
psql $BUILD_ENGINE --quiet --command "
  DROP TABLE IF EXISTS versions;
  CREATE TABLE versions ( 
    datasource text, 
    version text 
  );
"

#Import Data
import dcp_mappluto_wi
wait

rm -rf .library