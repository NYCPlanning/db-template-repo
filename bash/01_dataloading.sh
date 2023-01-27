#!/bin/bash
# Exit when any command fails
set -e
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
import dcp_mappluto_wi &

# Import GIS Features
import dcp_commercialoverlay &
import dcp_limitedheight &
import dcp_specialpurpose &
import dcp_specialpurposesubdistricts &
import dcp_zoningmapamendments &
import dcp_zoningdistricts &
import dcp_zoningmapindex &
wait

rm -rf .library