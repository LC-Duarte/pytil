#!/usr/bin/python3

"""
Project Name: Pytil
Description: A collection of useful tools and utilities for Python.
Author: Leonardo Duarte
Created on: May 28th, 2024
Version: 0.0.1
"""
import os
import sys

def search_file(file_name, search_dir="."):
    """
    Searches for a file with the given name in the specified directory or its subdirectories.

    Parameters:
        file_name (str): The name of the file to search for.
        search_dir (str, optional): The directory to start the search in. Defaults to the current directory.

    Returns:
        None

    Prints:
        The path of the file if it is found.

    Raises:
        None

    Example:
        >>> search_file("example.txt", "/path/to/directory")
        Found example.txt in /path/to/directory/example.txt
    """
    if not file_name:
        print("Please provide a file name to search for.")
        return

    if not search_dir:
        search_dir = "."

    for root, dirs, files in os.walk(search_dir):
        if file_name in files:
            print(f"Found {file_name} in {os.path.join(root, file_name)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python seek_file.py <file_name> [search_dir]")
        print("Searches recursively for a file based on the given name.")
        sys.exit(1)

    file_name = sys.argv[1]
    search_dir = sys.argv[2] if len(sys.argv) > 2 else "."

    search_file(file_name, search_dir)