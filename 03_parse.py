# -----------------------------------------------
#   3. Data Parsing:
# 
#   Objective: Parse course data leveraging
#   HTML elements structure.
# 
#   Tools/Resources: Use resources like the 
#   DOMParser, BeautifulSoup, or Regular Expressions.
#       Beautiful Soup:
#           https://www.crummy.com/software/BeautifulSoup/
#       DOMParser:
#           https://developer.mozilla.org/en-US/docs/Web/API/DOMParser
#       RegEx:
#           https://regexr.com 
#           https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions
# -----------------------------------------------

import re
from bs4 import BeautifulSoup

# Read in the HTML content
with open("combined_northeastern_catalog.html", "r") as file:  
    html_content = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_content, "html.parser")

# Find the div containing the course list
course_list_div = soup.find("div", id="atozindex")

# Extract each course group
course_groups = course_list_div.find_all("ul")

parsed_courses = []

for group in course_groups:
    # Extract the letter for this group
    letter = group.find_previous_sibling("h2").text.strip()

    # Extract each course in this group
    courses = group.find_all("a")
    for course in courses:
        # Extract course code and name
        full_name = course.text.strip()
        code = re.search(r"\((.*?)\)", full_name).group(1)
        name = re.sub(r"\(.*?\)", "", full_name).strip()

        # Extract URL (relative path)
        rel_url = course["href"]

        # Compile course info
        course_info = {
            "letter": letter,
            "code": code,
            "name": name,
            "rel_url": rel_url
        }

        parsed_courses.append(course_info)

# Write the parsed courses to a file
with open("parsed_courses.txt", "w") as file:
    for course in parsed_courses:
        file.write(str(course) + "\n")