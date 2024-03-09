#!/bin/bash

# Get the directory of the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Change directory to the script's directory
cd "$DIR"

# Get a list of files in the directory, excluding the script itself
SELF=$(basename "$0")
FILES=(*)
FILES=("${FILES[@]/$SELF}")

# Call the Python script with the filenames as arguments
python ../main.py 0 "${FILES[@]}"
python ../main.py 1 "${FILES[@]}"
