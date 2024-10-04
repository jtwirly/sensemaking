# -----------------------------------------------
#  9. Data pipeline:
# 
#  Write a program that automates the 
#  sequential execution of previously created 
#  script files, ensuring that each script 
#  runs to completion before the next begins. 
#  This program aims to streamline the 
#  generation of outputs from all your 
#  previous files, consolidating the 
#  results into one sequence.
# -----------------------------------------------

import subprocess
import sys
import os
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='pipeline.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_script(script_name):
    """
    Run a Python script and handle any errors.
    """
    try:
        logging.info(f"Starting execution of {script_name}")
        result = subprocess.run([sys.executable, script_name], 
                                check=True, 
                                capture_output=True, 
                                text=True)
        logging.info(f"Successfully completed {script_name}")
        print(f"Output from {script_name}:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error in {script_name}: {e}")
        logging.error(f"Error output: {e.output}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error in {script_name}: {e}")
        raise

def check_file_exists(filename):
    """
    Check if a file exists and log the result.
    """
    if os.path.exists(filename):
        logging.info(f"File {filename} exists.")
        return True
    else:
        logging.warning(f"File {filename} does not exist.")
        return False

def main():
    start_time = datetime.now()
    logging.info(f"Starting pipeline execution at {start_time}")

    scripts = [
        "01_pull.py",
        "02_combine.py",
        "03_parse.py",
        "04_clean.py",
        "05_extract.py",
        "06_frequency.py",
        "07_visualization.py",
        "08_export.py"
    ]

    try:
        for script in scripts:
            if check_file_exists(script):
                run_script(script)
            else:
                logging.error(f"Script {script} not found. Stopping pipeline.")
                break

        end_time = datetime.now()
        duration = end_time - start_time
        logging.info(f"Pipeline execution completed at {end_time}")
        logging.info(f"Total execution time: {duration}")
        print(f"Pipeline execution completed. Total time: {duration}")

    except Exception as e:
        logging.error(f"Pipeline execution failed: {e}")
        print(f"Pipeline execution failed. Check pipeline.log for details.")

if __name__ == "__main__":
    main()