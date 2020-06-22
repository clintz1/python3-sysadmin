#!/bin/sh

# Download and Install Python 3 from Source
yum groupinstall -y "development tools"
yum install -y \
  libffi-devel \
  zlib-devel \
  bzip2-devel \
  openssl-devel \
  ncurses-devel \
  sqlite-devel \
  readline-devel \
  tk-devel \
  gdbm-devel \
  db4-devel \
  libpcap-devel \
  xz-devel \
  expat-devel

cd /usr/src
wget http://python.org/ftp/python/3.6.4/Python-3.6.4.tar.xz
tar xf Python-3.6.4.tar.xz
cd Python-3.6.4
./configure --enable-optimizations
make altinstall

secure_path=/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/bin

# Upgrade Pip
pip3.6 install --upgrade pip
