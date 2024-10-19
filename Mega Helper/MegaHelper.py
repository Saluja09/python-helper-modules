import os
import logging
from datetime import datetime

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Helper function for file operations
def create_directory(directory_path):
    """
    Create a directory if it doesn't exist.
    
    :param directory_path: Path of the directory to create.
    :return: True if created or exists, False if there was an error.
    """
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            logging.info(f"Directory created: {directory_path}")
        else:
            logging.info(f"Directory already exists: {directory_path}")
        return True
    except Exception as e:
        logging.error(f"Failed to create directory: {e}")
        return False

def write_to_file(file_path, content):
    """
    Write content to a text file.
    
    :param file_path: Path to the file.
    :param content: The content to write into the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        logging.info(f"Content written to file: {file_path}")
    except Exception as e:
        logging.error(f"Failed to write to file: {e}")

def read_file(file_path):
    """
    Read and return the content of a text file.
    
    :param file_path: Path to the file to be read.
    :return: The file's content.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        logging.info(f"File read successfully: {file_path}")
        return content
    except Exception as e:
        logging.error(f"Failed to read file: {e}")
        return None

# Helper function for date formatting
def get_current_timestamp():
    """
    Get the current timestamp in 'YYYY-MM-DD HH:MM:SS' format.
    
    :return: Current timestamp as a string.
    """
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    return timestamp

def format_date(date_str, current_format, new_format):
    """
    Convert a date string from one format to another.
    
    :param date_str: Date string to format.
    :param current_format: Current format of the date string.
    :param new_format: Desired format of the date string.
    :return: Newly formatted date string.
    """
    try:
        date_obj = datetime.strptime(date_str, current_format)
        return date_obj.strftime(new_format)
    except ValueError as e:
        logging.error(f"Date formatting error: {e}")
        return None

# Helper function for string manipulations
def reverse_string(s):
    """
    Reverse a given string.
    
    :param s: String to reverse.
    :return: Reversed string.
    """
    return s[::-1]

def is_palindrome(s):
    """
    Check if a string is a palindrome (reads the same forward and backward).
    
    :param s: String to check.
    :return: True if palindrome, False otherwise.
    """
    clean_s = ''.join(e for e in s if e.isalnum()).lower()  # Ignore spaces and case
    return clean_s == clean_s[::-1]

def count_words(s):
    """
    Count the number of words in a string.
    
    :param s: String to count words in.
    :return: Word count as an integer.
    """
    return len(s.split())

# Helper function for logging
def log_info(message):
    """
    Log an info level message.
    
    :param message: The message to log.
    """
    logging.info(message)

def log_error(message):
    """
    Log an error level message.
    
    :param message: The error message to log.
    """
    logging.error(message)

def log_warning(message):
    """
    Log a warning level message.
    
    :param message: The warning message to log.
    """
    logging.warning(message)

# Example utility for list operations
def flatten_list(nested_list):
    """
    Flatten a nested list.
    
    :param nested_list: List that contains sublists.
    :return: A flat list.
    """
    return [item for sublist in nested_list for item in sublist]

# Sample execution when running this helper as a standalone script
if __name__ == "__main__":
    # Example usage of the helper functions
    log_info("Helper module is being executed directly.")
    
    # File operations
    create_directory('example_dir')
    write_to_file('example_dir/sample.txt', 'This is a test file.')
    content = read_file('example_dir/sample.txt')
    
    if content:
        print(f"File content: {content}")
    
    # Date formatting
    timestamp = get_current_timestamp()
    print(f"Current Timestamp: {timestamp}")
    
    formatted_date = format_date('2024-10-16', '%Y-%m-%d', '%d/%m/%Y')
    if formatted_date:
        print(f"Formatted Date: {formatted_date}")
    
    # String operations
    example_string = "madam"
    print(f"Is '{example_string}' a palindrome? {is_palindrome(example_string)}")
    
    reversed_string = reverse_string(example_string)
    print(f"Reversed String: {reversed_string}")
    
    # Logging warning
    log_warning("This is a warning log example.")
