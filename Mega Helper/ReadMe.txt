### README for Helper Module

---

# Mega Helper Module

## Overview
The **Helper Module** is a utility library that provides commonly used functions for file operations, date formatting, string manipulation, logging, and list operations. This module aims to simplify and streamline tasks that are frequently needed in Python projects. It can be reused across different projects to avoid redundant code.

## Features
The module includes the following features:

### 1. **File Operations**
   - `create_directory(directory_path)`: Creates a directory if it doesn't already exist.
   - `write_to_file(file_path, content)`: Writes content to a specified file.
   - `read_file(file_path)`: Reads content from a specified file.

### 2. **Date Formatting**
   - `get_current_timestamp()`: Returns the current timestamp in "YYYY-MM-DD HH:MM:SS" format.
   - `format_date(date_str, current_format, new_format)`: Converts a date from one format to another.

### 3. **String Manipulation**
   - `reverse_string(s)`: Reverses a given string.
   - `is_palindrome(s)`: Checks whether a string is a palindrome.
   - `count_words(s)`: Counts the number of words in a string.

### 4. **Logging**
   - `log_info(message)`: Logs an informational message.
   - `log_error(message)`: Logs an error message.
   - `log_warning(message)`: Logs a warning message.

### 5. **List Operations**
   - `flatten_list(nested_list)`: Flattens a nested list.

## How to Install

This module does not require any external dependencies apart from Python’s built-in libraries.

1. Clone the repository or download the `helper.py` file.
2. Place the `helper.py` file in your project directory.

## How to Use

To use this module, import it in your Python script or project:

```python
import helper

# Example usage of the helper functions

# Logging example
helper.log_info("Starting the process...")

# File operations example
helper.create_directory('example_dir')
helper.write_to_file('example_dir/sample.txt', 'This is a test file.')
content = helper.read_file('example_dir/sample.txt')

# Check if content was read successfully
if content:
    print(f"File content: {content}")

# Date formatting example
current_timestamp = helper.get_current_timestamp()
print(f"Current Timestamp: {current_timestamp}")

formatted_date = helper.format_date('2024-10-16', '%Y-%m-%d', '%d/%m/%Y')
if formatted_date:
    print(f"Formatted Date: {formatted_date}")

# String operations example
example_string = "madam"
print(f"Is '{example_string}' a palindrome? {helper.is_palindrome(example_string)}")

reversed_string = helper.reverse_string(example_string)
print(f"Reversed String: {reversed_string}")

# Flatten list example
nested_list = [[1, 2], [3, 4], [5]]
flat_list = helper.flatten_list(nested_list)
print(f"Flattened list: {flat_list}")
```

### Example Output:
```
2024-10-16 12:30:45 - INFO - Directory created: example_dir
2024-10-16 12:30:45 - INFO - Content written to file: example_dir/sample.txt
2024-10-16 12:30:45 - INFO - File read successfully: example_dir/sample.txt
File content: This is a test file.
Current Timestamp: 2024-10-16 12:30:45
Formatted Date: 16/10/2024
Is 'madam' a palindrome? True
Reversed String: madam
Flattened list: [1, 2, 3, 4, 5]
```

## Contributing

Feel free to contribute to this module by:
1. Adding new utility functions.
2. Optimizing the existing functions.
3. Reporting issues or suggesting improvements via GitHub issues.

## License

This helper module is open-source and free to use under the MIT License.

