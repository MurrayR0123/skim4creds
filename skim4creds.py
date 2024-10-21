#!/usr/bin/env python3
import os
from termcolor import colored

# Keywords to search for in the files
KEYWORDS = ["user", "password", "credential"]

# Function to highlight keywords in a line
def highlight_keywords(line, keyword):
    """
    Highlights occurrences of the keyword in the line.
    
    Arguments:
    - line: The line of text to be processed.
    - keyword: The keyword to highlight.
    
    Returns:
    The line with the keyword highlighted.
    """
    start_index = 0
    keyword_lower = keyword.lower()
    highlighted_line = ""

    # Case-insensitive search for the keyword and apply highlighting
    while True:
        index = line.lower().find(keyword_lower, start_index)
        if index == -1:
            highlighted_line += line[start_index:]  # Append the rest of the line if no more keywords are found
            break
        highlighted_line += line[start_index:index]  # Append the text before the keyword
        highlighted_line += colored(line[index:index + len(keyword)], 'red', attrs=['bold'])  # Highlight the keyword
        start_index = index + len(keyword)  # Move past the keyword
    return highlighted_line

# Function to search for keywords in a file
def search_keywords_in_file(file_path):
    """
    Opens a file and searches for any of the specified keywords.
    
    Arguments:
    - file_path: The path to the file to be searched.
    """
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line_number, line in enumerate(file, 1):  # Read file line by line with line numbers
                for keyword in KEYWORDS:
                    if keyword in line.lower():  # Check for keyword (case-insensitive)
                        print(f"Keyword '{keyword}' found in {file_path} on line {line_number}:")
                        print(highlight_keywords(line.strip(), keyword))  # Highlight and print the line
                        break  # Stop after the first match in a line
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")

# Recursive function to walk through directories
def search_in_directory(root_directory):
    """
    Recursively walks through directories and searches for keywords in files.
    
    Arguments:
    - root_directory: The directory from which the search should start.
    """
    for dirpath, _, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            search_keywords_in_file(file_path)

# Main entry point
if __name__ == "__main__":
    # Specify the directory to search in
    directory_to_search = input("Enter the directory to search: ")
    if os.path.isdir(directory_to_search):
        search_in_directory(directory_to_search)
    else:
        print(f"Directory '{directory_to_search}' does not exist.")
