# -----------------------------------------------
#  5. Data Extraction:
# 
#  Objective: Extract course titles from 
#  the data you cleaned.
# -----------------------------------------------
import ast

# Read in the cleaned data
with open("cleaned_courses.txt", "r") as file:
    cleaned_data = file.read()

# Split the cleaned data into individual course entries
course_entries = cleaned_data.strip().split("\n")

extracted_titles = []

for entry in course_entries:
    # Parse each course entry as a Python dictionary using ast.literal_eval()
    course_info = ast.literal_eval(entry)
    
    # Extract the course name
    name = course_info["name"]
    
    extracted_titles.append(name)

# Write the extracted titles to a file
with open("extracted_titles.txt", "w") as file:
    file.write("\n".join(extracted_titles))