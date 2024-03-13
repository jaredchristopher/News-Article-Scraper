"""
Created by: Jared Christopher
Module: run.py
Description: This module processes articles by retrieving HTML content from URLs stored in a file, 
saving the raw HTML to files in the 'raw' folder, and extracting article titles and text. 
The formatted article text is then written to corresponding text files in the 'processed' folder.
It creates the files if they do not already exist for the specific url.

Input:
- urls.txt: A text file containing URLs of articles to be processed.

Output:
- Raw HTML files: HTML content of each URL is written to separate files in the 'raw' directory.
- Processed text files: Formatted article text of each URL is written to separate files
  in the 'processed' directory.

Working:
1. Reads URLs from the 'urls.txt' file.
2. Fetches HTML content from each URL.
3. Extracts article title and text.
4. Writes HTML content to raw files and formatted text to processed files.
"""

import os
import textwrap
from module_1 import file_operations  # Importing file_operations module for file handling
from module_2 import html_parsing  # Importing html_parsing module for HTML content extraction

def main():
    # Define file paths and directories
    urls = 'urls.txt'  # File containing URLs
    raw_articles_directory = '/Users/jaredchristopher/CS325/Assignments/CS325_p2/Data/raw'  # Directory to store raw HTML files
    processed_articles_directory = '/Users/jaredchristopher/CS325/Assignments/CS325_p2/Data/processed'  # Directory to store processed text files

    # Create directories if they don't exist
    if not os.path.exists(raw_articles_directory):
        os.makedirs(raw_articles_directory)

    if not os.path.exists(processed_articles_directory):
        os.makedirs(processed_articles_directory)

    # Read URLs from the file
    urls_list = file_operations.URLReader.read_urls(urls)
    
    # Process each URL
    for i, url in enumerate(urls_list, start=1):
        # Fetch HTML content from the URL
        html_content = html_parsing.Fetch.fetch_html_content(url)
        
        # Write HTML content to raw file
        output_file_path = os.path.join(raw_articles_directory, f'article_{i}.html')
        file_operations.FileWriter.write_to_file(output_file_path, html_content)
        print(f'HTML content for URL {url} has been written to {output_file_path}')

        # Extract article title
        article_title = html_parsing.Article.extract_article_title(html_content)
        
        # Extract article text
        article_text = html_parsing.Article.extract_article_text(html_content)
        
        if article_text:
            # Format article text to fit within 80 characters per line
            formatted_text = textwrap.fill(article_text, width=80)
            
            # Add article title to the formatted text if available
            if article_title:
                formatted_text = f"Article Title: {article_title}\n\n{formatted_text}"
            
            # Write formatted text to the processed file
            processed_file_path = os.path.join(processed_articles_directory, f'article_{i}.txt')
            file_operations.FileWriter.write_to_file(processed_file_path, formatted_text)
            print(f'Formatted text for URL {url} has been written to {processed_file_path}')
        else:
            # If article text extraction fails, print a message and skip to the next URL
            print(f'Failed to extract article text for URL {url}. Skipping...')

if __name__ == "__main__":
    main()