#!/bin/sh

# Viewing Installed Packages
pip list
mkdir -p ~/.config/pip
vim ~/.config/pip/pip.conf
pip list

# Installing New Packages
pip install boto3

# Managing Required Packages with requirements.txt
pip freeze
pip freeze > requirements.txt
pip uninstall -y -r requirements.txt

# Installing Packages Local To Our User
pip install --user -r requirements.txt
pip list --user
pip uninstall boto3
