# -----------------------------------------------
#   4. Data Cleaning:
# 
#   Objective: Clean and preprocess the 
#   extracted data for analysis.
# 
#   Tools/Resources: Use Regular Expressions 
#   or string manipulation functions in 
#   your programming language.
# -----------------------------------------------
import re

# Read in the raw parsed data
with open("parsed_courses.txt", "r") as file:
    raw_data = file.read()

# Split the raw data into individual course entries
course_entries = re.findall(r"\{.*?\}", raw_data, re.DOTALL)

cleaned_courses = []

for entry in course_entries:
    # Remove any leading/trailing whitespace
    entry = entry.strip()

    # Remove the '(base) jt@dhcp-10-29-166-40 sensemaking-jtwirly % ' prefix if present
    entry = re.sub(r"^\(base\) jt@dhcp-10-29-166-40 sensemaking-jtwirly % ", "", entry)

    # Evaluate the cleaned entry as a Python dictionary
    course_info = eval(entry)

    # Fix the 'for Non-Law School Students' issue in the 'Law' entry
    if course_info["letter"] == "L" and course_info["code"] == "for Non-Law School Students":
        course_info["code"] = "LW"
        course_info["name"] = "Law (for Non-Law School Students)"

    cleaned_courses.append(course_info)

# Write the cleaned courses to a file
with open("cleaned_courses.txt", "w") as file:
    for course in cleaned_courses:
        file.write(str(course) + "\n")