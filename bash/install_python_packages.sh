#!/bin/bash
#
# Installs python packages required for building and testing pipeline.
set -e

# Install python requirements
python3 -m pip install --requirement requirements.txt
