#!/bin/bash
# A dev script used to compile and install python packages used in the dev container

# Install and update build requirements
python -m pip install --upgrade pip-tools pip wheel
# Delete exisitng requirements file
rm requirements.txt
# Compile requirements
CUSTOM_COMPILE_COMMAND="./dev_python_packages.sh" python -m piptools compile -o requirements.txt requirements.in
# Install requirements
python -m pip install --requirement requirements.txt
