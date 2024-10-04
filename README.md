# Sensemaking Problem Set: Course Catalog Data Cycle

This repository contains the code and analysis for the Sensemaking Problem Set, which provides a comprehensive exploration of the full data cycle, from collection to consumption, focusing on a public university course catalog. The problem set aims to develop skills in data acquisition, preparation, parsing, cleaning, extraction, analysis, visualization, and the creation of a clean, formatted dataset.

## Assignment Objectives
- Gain hands-on experience in data collection, storage, processing, and consumption
- Develop skills in analytics and visualization by working with a public university course catalog data

## Repository Structure

The repository is organized into the following structure:

- `01_pull.py`: Script for data acquisition, automating the process of accessing the website, navigating to the relevant sections if necessary, and downloading the HTML content.
- `02_combine.py`: Script for data preparation, combining multiple HTML files into a single comprehensive document.
- `03_parse.py`: Script for data parsing, extracting relevant information from the consolidated HTML document.
- `04_clean.py`: Script for data cleaning, refining the extracted information by removing or correcting any data that will break the parser.
- `05_extract.py`: Script for data extraction, identifying and extracting course titles from the cleaned dataset.
- `06_frequency.py`: Script for word frequency analysis, analyzing the most common words used in course titles.
- `07_visualization.py`: Script for data visualization, creating visual representations of the word frequencies obtained from the course titles.
- `08_export.py`: Script for exporting a clean, well-formatted dataset of the entire university catalog.
- `09_pipeline.py`: Script for automating the sequential execution of previously created script files.
- `10_mit_1996.json`: Extracted course data from the scanned 1996 MIT course catalog.
- `10_extract_1996.py`: Script for extracting course data from the scanned 1996 MIT course catalog.
- `11_mit_2024.json`: Extracted course data from the current MIT course catalog.
- `11_extract_2024.py`: Script for extracting course data from the current MIT course catalog.
- `12_course_offerings.py`: Script for analyzing the number of courses offered in various departments over time.
- `13_title_evolution.py`: Script for conducting a word frequency analysis on course titles from 1996 and 2024.
- `14_new_and_old.py`: Script for identifying subjects that were offered in 1996 but no longer exist in 2024, as well as new subjects introduced in 2024.
- `15_curriculum_breadth.py`: Script for comparing the breadth of topics in the 1996 and 2024 catalogs.
- `16_summary_reflection.txt`: Written summary reflecting on the most significant changes in the MIT course catalog over time.

## Setup and Usage

1. Clone the repository

2. Install the necessary dependencies. Refer to the individual script files for specific requirements.

3. Run the scripts in the specified order to perform the various stages of the data cycle.

4. Analyze the generated outputs, including the cleaned dataset, visualizations, and summary reflections.

## Submission

The problem set submission instructions can be found at:
https://classroom.github.com/a/MAgpvTrm

## Resources and References

- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/)
- [DOMParser Documentation](https://developer.mozilla.org/en-US/docs/Web/API/DOMParser)
- [RegEx Resources](https://regexr.com)
- [Mozilla Developer Network RegEx Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
- [Chart.js Official Website](https://www.chartjs.org/)
- [Google Charts Official Website](https://developers.google.com/chart/)
- [D3.js Official Website](https://d3js.org/)