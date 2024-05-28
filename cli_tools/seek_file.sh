#!/bin/bash


#Project Name: Pytil
#Description: A collection of useful tools and utilities for Python.
#Author: Leonardo Duarte
#Created on: May 28th, 2024#!/usr/bin/env python3
#
# Project Name: Pytil
# Description: A collection of useful tools and utilities for Python.
# Author: Leonardo Duarte
# Created on: May 28th, 2024
# Version: 0.0.1

import sys

# Your code goes here

if __name__ == "__main__":
    # Your main function goes here
    pass#!/usr/bin/env python3
    #
    # Project Name: Pytil
    # Description: A collection of useful tools and utilities for Python.
    # Author: Leonardo Duarte
    # Created on: May 28th, 2024
    # Version: 0.0.1
    
    import sys
    
    # Your code goes here
    
    if __name__ == "__main__":
        # Your main function goes here
        pass
#Version: 0.0.1



# Function to search recursively for a file
search_file() {
    file_name=$1
    search_dir=$2

    if [ -z "$file_name" ]; then
        echo "Please provide a file name to search for."
        return
    fi

    if [ -z "$search_dir" ]; then
        search_dir="."
    fi

    find "$search_dir" -type f -name "$file_name"
}

# Main program
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <file_name> [search_dir]"
    echo "Searches recursively for a file based on the given name."
    exit 1
fi

file_name=$1
search_dir=$2

search_file "$file_name" "$search_dir"