#!/bin/bash

python setup.py sdist bdist_wheel

pip install .

# INSTALL_DIR="/bin" 

# cp usr/bin "$INSTALL_DIR"

# chmod +x "$INSTALL_DIR/gwiz"

# echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> ~/.bashrc  
# source ~/.bashrc 

echo "Installation complete"
