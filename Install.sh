#!/bin/bash
# RanInfo Install Script
# Downloads all necessary files from GitHub

# URLs to your files on GitHub Releases
BASE_URL="https://github.com/SebPng/RanInfo/releases/download/v1.0.1"

FILES=("raninfo.py" "raninfo.png" "raninfo.desktop" "LICENSE" "README.md")

echo "Downloading RanInfo files..."

for file in "${FILES[@]}"; do
    echo "Downloading $file..."
    curl -L -o "$file" "$BASE_URL/$file" || { echo "Failed to download $file"; exit 1; }
done

chmod +x raninfo.py

echo "All files downloaded and raninfo.py is executable!"
echo "You can now run RanInfo using: ./raninfo.py"