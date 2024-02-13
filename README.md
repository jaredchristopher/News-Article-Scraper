# Web Scraping News Articles

This Python script fetches the HTML content of news articles from a list of URLs provided in a `urls.txt` file. It then extracts the article body and writes the content to their own text files. Each text file is named after the domain name of the news site. This is useful in organizing the text files by their name. For this project, however, we will only be using one news source, so their text file names are each followed by an index number to distiguish the different URLs.

## Building & Usage

1. **Clone the Repository**: Clone this repository to your local machine.

    Follow this link if you are unsure how to clone a repository:

    https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

2. **Install Dependencies**: Make sure you have Python 3 installed on your system. To set up the same environment I used to execute `scraper.py`, execute the one of the following commands in your console:

    ```
    conda create --name my_yaml_env --file requirement.yaml
    ```
    OR
    ```
    conda env create -f requirement.yaml
    ```
    *NOTE*: These commands will create a new Conda environment named `my_yaml_env` and install the dependencies specified in the `requirements.yaml` file. You do not need to execute both commands, just choose one. Also, you can name the environment whatever you like. I chose my_yaml_env for demonstration purposes.
    ```
    conda clean -p
    ```
    *NOTE*: This command removes unused packages and cached files from the Conda environment.

3. **Prepare URLs**: After setting up the environment, create a `urls.txt` file in the same directory as the script and add the URLs of the news articles you want to scrape. Copy and paste the entire URL in the text file, and make sure you use ONLY ONE URL per line.

4. **Run the Script**: Execute the `scraper.py` script using the command below. The script will fetch the HTML content for each URL, extract the article body, and write the content to text files.

    ```
    python3 scraper.py
    ```

5. **Check Output**: Check the generated text files in the same directory. Each text file contains the article content, wrapped at 50 characters per line. You can change the text wrapping size to your liking by modifying the width in the `textwrap.fill()` function (ex. `textwrap.fill(article_text, width = 60)`)

## Overall Notes

- Ensure that the URLs provided in `urls.txt` are valid and accessible.
- The script uses the `requests` library to fetch HTML content and `BeautifulSoup` for HTML parsing.
- Text files are named after the domain name of the news site and an index number for uniqueness.
- If no article body is found in the HTML content, the script skips that URL and prints the message.
- Check the console output for status messages and error notifications during execution. If you receive an error message, I recommend looking up the error to help you better understand why the fetching process failed.
- A more in-depth explination of the code is explained in my comments in my `scraper.py` file. 
