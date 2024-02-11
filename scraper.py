import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse # Extracts the URL's domain name
import textwrap # Makes the text files created not write to only one line


def main():
    # Opens and reads the urls.txt file
    with open('urls.txt', 'r') as file:
        urls = file.readlines()

    # Removes leading and trailing whitespace from each URL
    # I tired to not leave any whitespace but this is good for furture adjustments
    urls = [url.strip() for url in urls]

    # This for loop will fetch the HTML content for each URL
    for index, url in enumerate(urls, start = 1):
        try:
            response = requests.get(url)
            if response.status_code == 200: # Success status code
                # Process the HTML content
                html_content = response.text
                soup = BeautifulSoup(html_content, 'html.parser')
                
                # Extract the news site's domain name
                domain = urlparse(url).netloc
                # Replace the '.' with '_' so that the new names are vaild
                domain_name = domain.replace('.', '_')
                # New file name
                file_name = f'{domain_name}_{index}.txt'

                # Extract the content from JUST the article body
                article = soup.find('article')

                if article:
                    article_text = article.get_text()
                    formatted_text = textwrap.fill(article_text, width = 50) # Sets width to 50 in txt file
                    
                    # Write the HTML content to the text file for each respective news site
                    with open(file_name, 'w') as output_file:
                        output_file.write(formatted_text)
                    print(f"Article content for {url} written to {file_name}")
                else:
                    print(f"No article found for {url}. Skipping...")
            else:
                # If we could not fetch the URL, print the status code for the failure
                print(f"Failed to fetch {url}. Status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            # Throw an error for why the fetching failed
            print(f"An error occurred while fetching {url}: {e}")

if __name__ == "__main__":
    main()

                # # Extract article title if available
                # if soup.title is not None:
                #     article_title = soup.title.string.strip()

                #     # Replace special characters to make valid file name
                #     article_title = ''.join(c for c in article_title if c.isalnum() or c in [' ', '-'])
                # else:
                #     print(f"No title found for {url}. Skipping...")
