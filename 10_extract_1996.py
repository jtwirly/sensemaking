# -----------------------------------------------
#  10. Catalog 1996
# 
#  Extract course data from the scanned 
#  1996 MIT course catalog. After extracting 
#  the text, create a data model and save the 
#  processed data. This task emphasizes 
#  working with raw, scanned documents 
#  and aims to teach you how to extract 
#  information from non-digitized sources.
# -----------------------------------------------

# 10_extract_1996.py

"""
Script to extract course data from the scanned 1996 MIT course catalog PDF.
"""

import os
import json
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import re
from tqdm import tqdm

# Set up paths
PDF_FILE = 'mit_course_catalog_1996.pdf'  # Path to your downloaded PDF
OUTPUT_JSON = '10_mit_1996.json'

# Optional: Specify the path to tesseract executable if it's not in your PATH
# For example, on Windows:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def pdf_to_images(pdf_path):
    """
    Convert PDF pages to images.
    """
    print("Converting PDF pages to images...")
    images = convert_from_path(pdf_path)
    print(f"Converted {len(images)} pages into images.")
    return images

def ocr_images(images):
    """
    Perform OCR on a list of images.
    """
    print("Performing OCR on images...")
    text_pages = []
    for i, image in enumerate(tqdm(images, desc="OCR Processing")):
        text = pytesseract.image_to_string(image)
        text_pages.append(text)
    return text_pages

def extract_courses(text_pages):
    """
    Extract course data from OCR'd text.
    """
    print("Extracting courses from text...")
    courses = []
    course_pattern = re.compile(r'^(\d{1,3}\.[A-Za-z0-9]{1,3}[J]?)\s+(.+)', re.MULTILINE)
    description_pattern = re.compile(r'^[^\d]+', re.MULTILINE)

    for page_num, text in enumerate(text_pages):
        lines = text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            # Match course code and title
            match = course_pattern.match(line)
            if match:
                course_code = match.group(1)
                course_title = match.group(2).strip()
                description_lines = []
                i += 1
                # Collect description lines
                while i < len(lines):
                    desc_line = lines[i].strip()
                    # Stop if we reach another course or an empty line
                    if course_pattern.match(desc_line) or desc_line == '':
                        break
                    description_lines.append(desc_line)
                    i += 1
                course_description = ' '.join(description_lines).strip()
                courses.append({
                    'course_code': course_code,
                    'course_title': course_title,
                    'course_description': course_description,
                    'page_number': page_num + 1  # Pages are 1-indexed
                })
            else:
                i += 1  # Move to the next line if no match
    print(f"Extracted {len(courses)} courses.")
    return courses

def save_to_json(data, output_file):
    """
    Save data to a JSON file.
    """
    print(f"Saving data to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print("Data saved successfully.")

def main():
    # Step 1: Convert PDF to images
    images = pdf_to_images(PDF_FILE)

    # Step 2: Perform OCR on images
    text_pages = ocr_images(images)

    # Step 3: Extract courses from text
    courses = extract_courses(text_pages)

    # Step 4: Save data to JSON
    save_to_json(courses, OUTPUT_JSON)

if __name__ == '__main__':
    main()
