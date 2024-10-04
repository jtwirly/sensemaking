# -----------------------------------------------
#  11. Catalog 2024
# 
#  Extract course data from the current 
#  MIT course catalog. After extracting the 
#  text, create a data model and save the 
#  processed data.
# -----------------------------------------------

# 11_extract_2024.py

"""
Script to extract course data from the current MIT course catalog.
"""

import requests
from bs4 import BeautifulSoup
import json
import re
import time
import logging
import argparse

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Base URL for the MIT course catalog
BASE_URL = 'https://student.mit.edu/catalog'

def get_department_links():
    """
    Fetch the main catalog page and extract department links.

    Returns:
        list: List of full URLs to department pages.
    """
    index_url = f'{BASE_URL}/index.cgi'
    headers = {'User-Agent': 'Mozilla/5.0'}
    department_links = []

    try:
        response = requests.get(index_url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <a> tags that link to department pages
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            # Check if the link points to a department catalog page
            if re.match(r'^m\d{1,2}[a-z]\.html$', href):
                full_url = f'{BASE_URL}/{href}'
                department_links.append(full_url)

        # Remove duplicates
        department_links = list(set(department_links))
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching the main catalog page: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

    return department_links

def parse_department_page(dept_url):
    """
    Parse a department page to extract course data.

    Args:
        dept_url (str): URL of the department page.

    Returns:
        list: List of course dictionaries.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    courses = []

    try:
        response = requests.get(dept_url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        content = soup.find('body')
        if not content:
            logging.warning(f"No content found in {dept_url}")
            return courses

        elements = content.find_all(['h3', 'h4', 'p'])
        if not elements:
            logging.warning(f"No course elements found in {dept_url}")
            return courses

        current_course = {}
        for elem in elements:
            if elem.name in ['h3', 'h4']:
                # Start of a new course
                text = elem.get_text(separator=' ', strip=True)
                course_match = re.match(r'^(?P<course_code>[\d\w\.\-J]+)\s+(?P<course_title>.+)', text)
                if course_match:
                    if current_course:
                        courses.append(current_course)
                    current_course = {
                        'course_code': course_match.group('course_code'),
                        'course_title': course_match.group('course_title'),
                        'course_description': ''
                    }
            elif elem.name == 'p':
                # Course description or additional info
                if current_course:
                    desc = elem.get_text(separator=' ', strip=True)
                    desc = re.sub(r'\s+', ' ', desc)  # Normalize whitespace
                    current_course['course_description'] += ' ' + desc
        # Add the last course
        if current_course:
            courses.append(current_course)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching department page {dept_url}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error in parsing {dept_url}: {e}")

    return courses

def main():
    parser = argparse.ArgumentParser(description='Extract MIT course catalog data.')
    parser.add_argument('--output', default='11_mit_2024.json', help='Output JSON file')
    args = parser.parse_args()

    logging.info("Fetching department links...")
    department_links = get_department_links()
    logging.info(f"Found {len(department_links)} department pages.")

    all_courses = []
    visited_urls = set()

    for dept_url in department_links:
        if dept_url in visited_urls:
            continue
        visited_urls.add(dept_url)
        logging.info(f"Processing {dept_url}...")
        courses = parse_department_page(dept_url)
        logging.info(f"Extracted {len(courses)} courses from this department.")
        all_courses.extend(courses)
        time.sleep(1)  # Be polite and avoid overwhelming the server

    logging.info(f"Total courses extracted: {len(all_courses)}")

    # Save the data to JSON
    try:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(all_courses, f, indent=2)
        logging.info(f"Course data saved to {args.output}")
    except Exception as e:
        logging.error(f"Error saving data to JSON: {e}")

if __name__ == '__main__':
    main()
