#!/bin/bash

# Directory to iterate over, replace '/path/to/directory' with your actual directory path
DIRECTORY='../part-02-data-types-and-structures/'

# Check if the directory exists
if [ -d "$DIRECTORY" ]; then
  # Use find to loop through all files in the directory and its subdirectories
  find "$DIRECTORY" -type f -exec echo "Contents of {}:" \; -exec cat "{}" \; -exec echo \;
else
  echo "Directory does not exist."
fi
