# -----------------------------------------------
#  12. Course Offerings Over Time
# 
#  After extracting the course data from 
#  both the 1996 and present catalogs, 
#  analyze the number of courses offered 
#  in various departments. Are there any 
#  departments that have significantly 
#  expanded or reduced their course offerings? 
#  If so, identify them and discuss possible 
#  reasons for these changes.
# -----------------------------------------------

# 12_course_offerings.py

"""
Script to analyze course offerings over time between 1996 and 2024.
"""

import json
from collections import defaultdict
import matplotlib.pyplot as plt
import logging
import csv
import math

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_json_data(file_path):
    """
    Load JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: Loaded JSON data as a list of dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"Error loading JSON data from {file_path}: {e}")
        return []

def extract_department(course_code):
    """
    Extract department code from course code.

    Args:
        course_code (str): Course code string.

    Returns:
        str: Extracted department code.
    """
    match = re.match(r'^([A-Za-z]*\d+)', course_code)
    return match.group(1) if match else 'Unknown'

def count_courses_by_department(courses, code_key):
    """
    Count the number of courses by department.

    Args:
        courses (list): List of course dictionaries.
        code_key (str): Key in the dictionary for course code.

    Returns:
        dict: Dictionary with department codes as keys and counts as values.
    """
    department_counts = defaultdict(int)
    for course in courses:
        if code_key in course and course[code_key]:
            dept = extract_department(course[code_key])
            department_counts[dept] += 1
    return dict(department_counts)

def compare_departments(dept_counts_1996, dept_counts_2024):
    """
    Compare course counts between 1996 and 2024.

    Args:
        dept_counts_1996 (dict): Department counts from 1996.
        dept_counts_2024 (dict): Department counts from 2024.

    Returns:
        dict: Dictionary with departments as keys and tuples of (change, percent_change).
    """
    all_depts = set(dept_counts_1996.keys()) | set(dept_counts_2024.keys())
    changes = {}
    for dept in all_depts:
        count_1996 = dept_counts_1996.get(dept, 0)
        count_2024 = dept_counts_2024.get(dept, 0)
        change = count_2024 - count_1996
        if count_1996 > 0:
            percent_change = (change / count_1996) * 100
        elif count_2024 > 0:
            percent_change = 100.0  # New department
        else:
            percent_change = 0.0
        changes[dept] = (change, percent_change)
    return changes

def plot_changes(changes):
    """
    Plot the percentage changes in course offerings.

    Args:
        changes (dict): Dictionary of department changes.
    """
    depts = list(changes.keys())
    percent_changes = [changes[dept][1] for dept in depts]

    # Limit the y-axis to improve readability
    plt.figure(figsize=(12, 6))
    plt.bar(depts, percent_changes)
    plt.title('Percentage Change in Course Offerings by Department (1996 to 2024)')
    plt.xlabel('Department')
    plt.ylabel('Percentage Change (%)')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('department_changes.png')
    plt.close()

def save_changes_to_csv(changes):
    """
    Save department changes to a CSV file.

    Args:
        changes (dict): Dictionary of department changes.
    """
    try:
        with open('department_changes.csv', 'w', newline='') as csvfile:
            fieldnames = ['Department', 'Change', 'PercentChange']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for dept, (change, percent_change) in changes.items():
                writer.writerow({'Department': dept, 'Change': change, 'PercentChange': percent_change})
        logging.info("Department changes saved to 'department_changes.csv'")
    except Exception as e:
        logging.error(f"Error saving changes to CSV: {e}")

def save_insights_to_file(sorted_changes):
    """
    Save the insights about significant changes in course offerings to a file.

    Args:
        sorted_changes (list): List of (department, (change, percent_change)) tuples, sorted by percent change.
    """
    try:
        with open('course_offerings_insights.txt', 'w') as f:
            f.write("Departments with significant changes in course offerings:\n\n")
            for dept, (change, percent_change) in sorted_changes:
                if abs(percent_change) >= 50:  # Threshold for "significant" change
                    f.write(f"{dept}: {percent_change:.2f}% change ({change} courses)\n")
                    if percent_change > 0:
                        f.write("  Possible reasons for increase:\n")
                        f.write("  - Growing demand and interest in the field\n")
                        f.write("  - Expansion of research and specializations\n")
                        f.write("  - Interdisciplinary collaborations and applications\n")
                    else:
                        f.write("  Possible reasons for decrease:\n")
                        f.write("  - Shift in academic focus and priorities\n")
                        f.write("  - Consolidation or restructuring of programs\n")
                        f.write("  - Decreased student enrollment or interest\n")
                    f.write("\n")
        logging.info("Insights saved to 'course_offerings_insights.txt'")
    except Exception as e:
        logging.error(f"Error saving insights to file: {e}")

def main():
    # Load data
    data_1996 = load_json_data('10_mit_1996.json')
    data_2024 = load_json_data('11_mit_2024.json')
    if not data_1996 or not data_2024:
        logging.error("Data loading failed. Exiting.")
        return

    # Count courses by department
    dept_counts_1996 = count_courses_by_department(data_1996, 'course_code')

    # Determine the correct key for 2024 data
    if 'course_number' in data_2024[0]:
        key_2024 = 'course_number'
    elif 'course_code' in data_2024[0]:
        key_2024 = 'course_code'
    else:
        logging.error("Unable to find course code in 2024 data")
        return

    dept_counts_2024 = count_courses_by_department(data_2024, key_2024)

    # Compare departments
    changes = compare_departments(dept_counts_1996, dept_counts_2024)

    # Sort changes by percentage
    sorted_changes = sorted(changes.items(), key=lambda x: x[1][1], reverse=True)

    # Save insights to file
    save_insights_to_file(sorted_changes)

    # Plot changes
    plot_changes(changes)
    logging.info("Visualization saved as 'department_changes.png'")

    # Save changes to CSV
    save_changes_to_csv(changes)

if __name__ == "__main__":
    import re
    main()

"""
Departments with significant changes in course offerings:

20: 2850.00% change (57 courses)
  Possible reasons for increase:
  - Growing demand and interest in the field
  - Expansion of research and specializations
  - Interdisciplinary collaborations and applications

Unknown: 100.00% change (10 courses)
  Possible reasons for increase:
  - Growing demand and interest in the field
  - Expansion of research and specializations
  - Interdisciplinary collaborations and applications

18: -58.74% change (-121 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

12: -59.12% change (-107 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

16: -59.70% change (-80 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

2: -60.27% change (-88 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

11: -63.89% change (-92 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

5: -65.05% change (-67 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

4: -66.88% change (-103 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

22: -68.18% change (-75 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

9: -68.67% change (-57 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

15: -70.69% change (-164 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

1: -72.19% change (-135 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

6: -74.88% change (-155 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

17: -75.00% change (-96 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

13: -100.00% change (-97 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

44: -100.00% change (-1 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

48: -100.00% change (-2 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

211: -100.00% change (-1 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

43: -100.00% change (-2 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

42: -100.00% change (-1 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

72: -100.00% change (-1 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

215: -100.00% change (-1 courses)
  Possible reasons for decrease:
  - Shift in academic focus and priorities
  - Consolidation or restructuring of programs
  - Decreased student enrollment or interest

"""