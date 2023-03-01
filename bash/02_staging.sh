#!/bin/bash
source bash/build_config.sh

echo "Dataset Version $VERSION : 02 Staging"

echo "Preprocess source data ..."
run_sql_file sql/preprocessing.sql

echo "Done!"
