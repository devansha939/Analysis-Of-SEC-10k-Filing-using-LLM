import os
import nltk
from bs4 import BeautifulSoup
from sec_edgar_downloader import Downloader

from bs4 import BeautifulSoup

def extract_text_from_html(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'lxml')  # Using lxml instead of html.parser
            text_content = soup.get_text(separator='\n', strip=True)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text_content)
        print(f"Successfully processed {file_path}")
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

def process_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.txt'):
                full_path = os.path.join(root, file)
                print(f"Attempting to extract text from {full_path}")
                extract_text_from_html(full_path)

def download_10k(ticker):
    download_path = os.path.join(os.getcwd(), "sec_filings")
    dl = Downloader(download_path, "2021eeb1164@iitrpr.ac.in")

    for year in range(1995, 2024):
        # Download the 10-K filings for the specified ticker and year.
        dl.get("10-K", ticker, after=f"{year}-01-01", before=f"{year}-12-31")

        # Set the expected path for the filings
        filings_path = os.path.join(download_path, "sec-edgar-filings", ticker, "10-K")

        # Check if the filings directory exists before processing
        if not os.path.exists(filings_path):
            print(f"No filings found for {ticker} in {year}")
            continue  # Skip to the next year if no filings directory

        for filing_year_folder in os.listdir(filings_path):
            full_year_path = os.path.join(filings_path, filing_year_folder)
            html_files = [f for f in os.listdir(full_year_path) if f.endswith('.html')]
            for html_file in html_files:
                file_path = os.path.join(full_year_path, html_file)
                with open(file_path, 'r', encoding='utf-8') as file:
                    soup = BeautifulSoup(file, 'html.parser')
                    text_content = soup.get_text(separator=' ', strip=True)

                text_file_path = file_path.replace('.html', '.txt')
                with open(text_file_path, 'w', encoding='utf-8') as text_file:
                    text_file.write(text_content)

nltk.download('punkt')
nltk.download('stopwords')

if __name__ == "__main__":
    tickers = input("Enter company tickers, separated by space: ").split()
    
    for ticker in tickers:
        print(f"Downloading 10-K filings for {ticker}...")
        download_10k(ticker)
    print("Download complete!")

    directory_path = 'sec-edgar-filings/AAPL/10-K'
    process_directory(directory_path)
    print("Text extraction and overwrite completed for all files.")
