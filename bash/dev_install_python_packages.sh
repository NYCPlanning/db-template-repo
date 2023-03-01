#!/bin/bash
# A dev script used to install python packages to be used in a virtual environment or dev container
set -e

# Install requirements
python3 -m pip install --requirement requirements.txt
