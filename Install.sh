#!/usr/bin/env bash

echo "Installing RanInfo..."

# create install directory
mkdir -p "$HOME/RanInfo"

# go into it
cd "$HOME/RanInfo"

# download latest raninfo script
curl -L https://raw.githubusercontent.com/SebPng/RanInfo/main/raninfo.py -o raninfo

# make executable
chmod +x raninfo

# add to PATH if not already there
if ! grep -q 'RanInfo' "$HOME/.bashrc"; then
    echo 'export PATH="$HOME/RanInfo:$PATH"' >> "$HOME/.bashrc"
fi

echo ""
echo "RanInfo installed in ~/RanInfo"
echo "Restart terminal or run:"
echo "source ~/.bashrc"
echo ""
echo "Then you can use:"
echo "raninfo --name"
echo "raninfo --pass"
echo "raninfo --pass --length 20"
echo "raninfo -h/--help