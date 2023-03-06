#!/bin/bash
# A script used by build scripts to import utility functions, set environment variables,
# and configure connections

source bash/build_utils.sh

# Set environemnt variables from .env files
set_env .env version.env

# # Set environemnt variables from BUILD_ENGINE url
# urlparse $BUILD_ENGINE

# Add an S3-compatible service to the MinIO configuration with alias "spaces"
mc config host add spaces $DO_S3_ENDPOINT $DO_ACCESS_KEY_ID $DO_SECRET_ACCESS_KEY --api S3v4
