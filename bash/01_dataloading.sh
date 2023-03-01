#!/bin/bash
source bash/build_config.sh

echo "Dataset Version $VERSION : 01 Data Loading"

# Create a versions table with source dataset versions
echo "Create versions table ..."
run_sql_command "
  DROP TABLE IF EXISTS versions;
  CREATE TABLE versions ( 
    datasource text, 
    version text 
  );
"

# Import data
echo "Import source data ..."
import dcp_zoningdistricts

# # Delete data cache (optional)
# echo "Deleting source data cache ..."
# rm -rf .library

echo "Done!"
