#!/usr/bin/env bash

# Create directory
mkdir -p ~/RanInfo

# Navigate into it
cd ~/RanInfo || exit

# Download the latest raninfo.py from GitHub
curl -LO https://raw.githubusercontent.com/SebPng/RanInfo/main/raninfo.py

# Make it executable
chmod +x raninfo.py

# Add to PATH if not already
PROFILE_FILE="$HOME/.bashrc"
if ! grep -q 'export PATH="$HOME/RanInfo:$PATH"' "$PROFILE_FILE"; then
    echo 'export PATH="$HOME/RanInfo:$PATH"' >> "$PROFILE_FILE"
    echo "Added ~/RanInfo to PATH in $PROFILE_FILE"
fi

echo "Installation complete! You may need to restart your terminal or run 'source ~/.bashrc'."
echo "You can now run the command 'raninfo.py --help'"