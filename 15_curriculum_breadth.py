# -----------------------------------------------
#  15. Curriculum Breadth:
# 
#  Compare the breadth of topics in the 
#  1996 and 2024 catalogs to assess whether 
#  the curriculum has become more 
#  interdisciplinary or specialized.
# -----------------------------------------------

import json
import re

def extract_department(course_code):
    digits = re.findall(r'\d+', course_code)
    return digits[0] if digits else 'Unknown'

# Read in the 1996 and 2024 MIT course catalog JSON files
with open('10_mit_1996.json') as f:
    data_1996 = json.load(f)

with open('11_mit_2024.json') as f:  
    data_2024 = json.load(f)

# Extract department numbers from course codes
depts_1996 = [extract_department(d['course_code']) for d in data_1996]
depts_2024 = [extract_department(d['course_code']) for d in data_2024]

# Count unique departments represented each year
unique_depts_1996 = len(set(depts_1996))
unique_depts_2024 = len(set(depts_2024))

print(f"Unique departments in 1996: {unique_depts_1996}")
print(f"Unique departments in 2024: {unique_depts_2024}")

# Classify subjects as interdisciplinary if their title contains "and", "innovation", etc.
def is_interdisciplinary(title):
    keywords = ['and', 'innovation', 'synthe', 'integrat', 'application', 'multidisciplin', 'crossdisciplin', 'transdisciplin', 'interdisciplin']
    return any(word in title.lower() for word in keywords)

interdisciplinary_1996 = sum(is_interdisciplinary(d['course_title']) for d in data_1996)
interdisciplinary_2024 = sum(is_interdisciplinary(d['course_title']) for d in data_2024)

print(f"\nInterdisciplinary subjects in 1996 (based on titles): {interdisciplinary_1996} ({interdisciplinary_1996/len(data_1996):.2%})")  
print(f"Interdisciplinary subjects in 2024 (based on titles): {interdisciplinary_2024} ({interdisciplinary_2024/len(data_2024):.2%})")

# Unique departments in 1996: 29
#Unique departments in 2024: 22

# Interdisciplinary subjects in 1996 (based on titles): 709 (25.30%)
# Interdisciplinary subjects in 2024 (based on titles): 378 (31.27%)

# not 100% sure about this - should I use course descriptions?