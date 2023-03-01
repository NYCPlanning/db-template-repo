#!/bin/bash
# A dev script used to compile and install python packages
# to be used in a virtual environment or dev container
set -e

# UNCOMMENT TO RECOMPILE requirements.txt
# Install and update build requirements
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pip-tools wheel

# Delete exisitng requirements file
rm requirements.txt
# Compile requirements
CUSTOM_COMPILE_COMMAND="./bash/dev_python_packages.sh" python3 -m piptools compile --output-file=requirements.txt requirements.in

# Install requirements
python3 -m pip install --requirement requirements.txt
