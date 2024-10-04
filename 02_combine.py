# -----------------------------------------------
#  2. Data Preparation:
# 
#  Objective: Combine multiple HTML files into 
#  a single document.
# 
#  Tools/Resources: Concatenate HTML text using 
#  python or javascript.
# -----------------------------------------------

import os
from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_html_file(file_path):
    """Read an HTML file and return its content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return None

def extract_main_content(html_content):
    """Extract the main content from an HTML file."""
    soup = BeautifulSoup(html_content, 'html.parser')
    main_content = soup.find('div', id='textcontainer')
    return str(main_content) if main_content else ''

def combine_html_files(input_dir, output_file):
    """Combine HTML files from the input directory into a single document."""
    combined_content = []
    
    # Get all HTML files in the input directory
    html_files = [f for f in os.listdir(input_dir) if f.endswith('.html')]
    
    for filename in html_files:
        file_path = os.path.join(input_dir, filename)
        html_content = read_html_file(file_path)
        if html_content:
            main_content = extract_main_content(html_content)
            if main_content:
                combined_content.append(f"<!-- Start of {filename} -->\n{main_content}\n<!-- End of {filename} -->")
            else:
                logging.warning(f"No main content found in {filename}")
    
    # Create a well-formed HTML document with the combined content
    combined_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Combined Northeastern University Course Catalog</title>
    </head>
    <body>
    {''.join(combined_content)}
    </body>
    </html>
    """

    # Write the combined content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(combined_html)

    logging.info(f"Combined HTML file created: {output_file}")

def main():
    input_dir = 'raw_html/northeastern'
    output_file = 'combined_northeastern_catalog.html'
    combine_html_files(input_dir, output_file)

if __name__ == "__main__":
    main()