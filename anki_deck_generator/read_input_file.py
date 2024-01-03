import os
import logging
import textract


def convert_file_to_text(file_path):
    if not os.path.exists(file_path):
        logging.error(f"The file {file_path} does not exist.")
        return None

    try:
        text = textract.process(file_path)
        return text
    except Exception as e:
        logging.error(f"An error occurred while reading the file: {e}")
