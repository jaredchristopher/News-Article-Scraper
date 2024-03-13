"""
Created by: Jared Christopher
Module: html_parsing.py
Description: This module provides functionality for parsing HTML content and extracting article text and titles.

ArticleParser:
- extract_article_text(html_content): Abstract method for extracting article text from HTML content.
- extract_article_title(html_content): Abstract method for extracting article title from HTML content.

Article:
- extract_article_text(html_content): Extracts article text from the provided HTML content.
Args:
- html_content: HTML content of the article.
Returns:
- Extracted article text or None if not found.
  
- extract_article_title(html_content): Extracts article title from the provided HTML content.
Args:
- html_content: HTML content of the article.
Returns:
- Extracted article title or None if not found.

Fetch:
- fetch_html_content(url): Fetches HTML content from the provided URL.
Args:
- url: URL of the article.
Returns:
- HTML content of the article or raises an exception if the request fails.
"""
import requests
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

class ArticleParser(ABC):
    @abstractmethod
    def extract_article_text(self, html_content):
        pass

    @abstractmethod
    def extract_article_title(self, html_content):
        pass

class Article(ArticleParser):
    # Extracts article text from HTML content.
    def extract_article_text(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        article = soup.find('article')
        if article:
            return article.get_text()
        else:
            return None
        
    # Extracts article title from HTML content.
    def extract_article_title(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.find('title')
        if title:
            return title.get_text()
        else:
            return None

class Fetch:
    # Fetches HTML content from a URL.
    def fetch_html_content(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return requests.exceptions.RequestException(f"Failed to {url}. Status code {response.status_code}")