# -----------------------------------------------
#  8. Export a Clean Formatted Dataset
#  of the Entire University Catalog:
# 
#  Export a Clean Formatted Dataset of 
#  the Entire University Catalog: The 
#  dataset you would have liked when you 
#  started. Prepare and export a clean, 
#  well-formatted dataset encompassing 
#  the entire university catalog. This 
#  dataset should be in a form that is 
#  readily usable for analysis and 
#  visualization, reflecting the cleaned 
#  and consolidated data you've worked 
#  with throughout the project. Document 
#  the structure of your dataset, including 
#  a description of columns, data types, and 
#  any assumptions or decisions made during 
#  the data preparation process.
# -----------------------------------------------

import json
from datetime import datetime

def load_data(file_path):
    """Load data from the cleaned_courses.txt file."""
    courses = []
    with open(file_path, 'r') as file:
        for line in file:
            course = eval(line)
            courses.append(course)
    return courses

def clean_data(courses):
    """Clean and format the data."""
    cleaned_courses = []
    for course in courses:
        cleaned_course = {
            "letter": course["letter"],
            "code": course["code"],
            "name": course["name"],
            "rel_url": course["rel_url"]
        }
        cleaned_courses.append(cleaned_course)
    return cleaned_courses

def format_as_json(courses):
    """Format the courses as a JSON structure."""
    catalog = {
        "university_name": "Northeastern University",
        "catalog_year": datetime.now().year,
        "last_updated": datetime.now().isoformat(),
        "courses": courses
    }
    return catalog

def export_json(data, file_path):
    """Export data as a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    input_file = 'cleaned_courses.txt'
    output_file = 'university_catalog.json'
    
    # Load data
    courses = load_data(input_file)
    
    # Clean and format data
    clean_courses = clean_data(courses)
    
    # Format as JSON
    catalog_json = format_as_json(clean_courses)
    
    # Export JSON
    export_json(catalog_json, output_file)
    
    print(f"Clean, formatted dataset exported to {output_file}")

if __name__ == "__main__":
    main()