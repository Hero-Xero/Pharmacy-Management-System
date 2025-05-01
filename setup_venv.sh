#!/bin/bash

# Exit on any error
set -e

# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found."
    exit 1
fi
