# -----------------------------------------------
#  1. Data Acquisition:
# 
#  Objective: Download all the public course 
#  catalog data in raw HTML format from a 
#  university website.
# 
#  Tools/Resources: Extract all the course 
#  catalog data from one of the follow 
#  three universities:
#     Harvard: https://courses.my.harvard.edu
#     BU: https://www.bu.edu/academics/cas/courses
#     NE: https://catalog.northeastern.edu/course-descriptions
# -----------------------------------------------

import requests
from bs4 import BeautifulSoup
import os
import time
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_page(url, filename):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        logging.info(f"Downloaded: {filename}")
        return response.text
    except requests.RequestException as e:
        logging.error(f"Failed to download {url}: {e}")
        return None

def download_northeastern():
    base_url = "https://catalog.northeastern.edu"
    catalog_url = f"{base_url}/course-descriptions/"
    output_dir = "raw_html/northeastern"
    os.makedirs(output_dir, exist_ok=True)

    try:
        response = requests.get(catalog_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        course_links = soup.find_all('a', class_='levelthree')

        for link in course_links:
            department_url = base_url + link['href']
            department_name = link.text.strip().replace(' ', '_')
            filename = f"{output_dir}/{department_name}.html"
            content = download_page(department_url, filename)
            if content:
                time.sleep(1)  # Be polite to the server
            else:
                logging.warning(f"Failed to download {department_name}")

        logging.info("Northeastern download complete!")
    except requests.RequestException as e:
        logging.error(f"An error occurred while downloading Northeastern courses: {e}")

def main():
    logging.info("Starting Northeastern course catalog download...")
    download_northeastern()
    logging.info("Download complete!")

if __name__ == "__main__":
    main()