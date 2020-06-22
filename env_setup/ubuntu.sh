#!/bin/sh

# Download and Install Python 3 from Source
apt update -y
apt install -y \
  wget \
  build-essential \
  libssl-dev \
  zlib1g-dev \
  libbz2-dev \
  libreadline-dev \
  libsqlite3-dev \
  libncurses5-dev \
  libncursesw5-dev \
  xz-utils \
  tk-dev

cd /usr/src
wget http://python.org/ftp/python/3.6.4/Python-3.6.4.tar.xz
tar xf Python-3.6.4.tar.xz
cd Python-3.6.4
./configure --enable-optimizations
make altinstall

secure_path=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin

# Upgrade Pip
pip3.6 install --upgrade pip
