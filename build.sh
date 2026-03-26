#!/bin/bash
set -e

echo "Installing system dependencies..."
apt-get update && apt-get install -y cmake build-essential libssl-dev git

echo "Cloning and building liboqs..."
git clone https://github.com/open-quantum-safe/liboqs
cd liboqs
mkdir build && cd build
cmake -DOQS_BUILD_ONLY_LIB=ON ..
make -j
make install
ldconfig
cd ../../

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Build completed!"
