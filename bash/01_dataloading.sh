#!/bin/bash
source bash/build_config.sh

# Create a versions table with source dataset versions
psql $BUILD_ENGINE --quiet --command "
  DROP TABLE IF EXISTS versions;
  CREATE TABLE versions ( 
    datasource text, 
    version text 
  );
"

# Import data
import dcp_zoningdistricts

# Delete data cache (optional)
rm -rf .library
