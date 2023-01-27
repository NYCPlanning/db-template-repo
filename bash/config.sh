#!/bin/bash
# Exit when any command fails
set -e
# keep track of the last executed command
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
# echo an error message before exiting
trap 'echo "\"${last_command}\" command filed with exit code $?."' EXIT

source bash/utils.sh

# Set Environmental Variables
set_env .env version.env

# Parse database url
urlparse $BUILD_ENGINE

# Add an S3-compatible service to the MinIO configuration with alias "spaces"
mc config host add spaces $AWS_S3_ENDPOINT $AWS_ACCESS_KEY_ID $AWS_SECRET_ACCESS_KEY --api S3v4
