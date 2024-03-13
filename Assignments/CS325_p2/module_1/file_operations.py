"""
Created by: Jared Christopher
Module: file_operations.py
Description: This module contains classes URLReader and FileWriter, each with a single responsibility.
The URLReader class is responsible for reading URLs from a file, while the FileWriter class is responsible
for writing content to a file.

URLReader:
- read_urls(filename): Reads URLs from the specified file and returns them as a list after stripping
  whitespace from each URL.

FileWriter:
- write_to_file(filename, content): Writes the provided content to the specified file.
"""

import textwrap

class URLReader:
    # Reads URLs from the specified file and returns them as a list.
    # filename: path to the file to write to
    def read_urls(filename):
        with open(filename, 'r') as file:
            urls = file.readlines()
        return [url.strip() for url in urls]

class FileWriter:
    # filename: path to the file to write to
    # content: content to write to file (text & title)
    def write_to_file(filename, content):
        with open(filename, 'w') as ftwt:
            ftwt.write(content)
