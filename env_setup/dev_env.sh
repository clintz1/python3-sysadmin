#!/bin/sh

# Installing Packages
yum update
yum groupinstall -y "development tools"
yum install -y lsof wget vim-enhanced words which

# Configuring Git
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"

# Customizing Bash
curl https://raw.githubusercontent.com/linuxacademy/content-python3-sysadmin/master/helpers/bashrc -o ~/.bashrc

# Customizing Vim
curl https://raw.githubusercontent.com/linuxacademy/content-python3-sysadmin/master/helpers/vimrc -o ~/.vimrc
