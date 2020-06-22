#!/bin/sh

# Virtualenv or Venv
python -m venv [PATH FOR VIRTUALENV]
mkdir venvs
python -m venv venvs/experiment
source venvs/experiment/bin/activate
echo $PATH
which python
python --version
pip list
deactivate
