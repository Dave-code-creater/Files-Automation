# Files_Automation
# File Organizer Script

This is a Python script designed to organize files in a directory based on their file extensions. It categorizes files into subdirectories according to a predefined mapping of file extensions to directory names.

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Usage](#usage)
- [File Types Mapping](#file-types-mapping)
- [Customization](#customization)
- [Advanced Usage](#advanced-usage)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Overview

In our digital age, managing files efficiently is crucial. This script aims to simplify the task of organizing files by automating the process. It examines the file extensions of each file in a specified directory and moves them to the appropriate subdirectory based on a predefined mapping.

The idea behind this script is to bring order to your cluttered directories, making it easier to locate and manage your files. Whether you're dealing with a chaotic downloads folder or a disorganized collection of documents, this script can help streamline your file management.

## Requirements

To use this script, you need the following:

- Python 3.x: The script is written in Python, so you must have a Python interpreter installed on your system.

- Required Libraries: The script uses standard Python libraries such as `os` and `shutil`, which are typically included with Python installations.

## Usage

1. **Download the Script**: Clone or download the script to your computer using the provided link.

2. **Open the Script**: You can use any text editor or Python Integrated Development Environment (IDE) to open the script.

3. **Customize the Mapping**: Customize the `File_Types` dictionary to match your desired file organization structure. This dictionary associates file extensions with directory names. For example:

   ```python
   File_Types = {
       ".jpg": "Pictures",
       ".pdf": "Documents",
       ".mp3": "Music",
       # Add more extensions and directories as needed
   }
Specify the Target Directory: Modify the Change_Directory() function to specify the directory you want to organize. By default, it's set to 'C:/Users/Admin/Downloads'. Replace this path with the path of your target directory.

Save Your Changes: Ensure you save the script after making any modifications.

Run the Script: Open a command prompt or terminal, navigate to the directory where the script is located, and run the script by executing:
python script.py
Organization Process: The script will analyze each file in the target directory, determine its file extension, and move it to the appropriate subdirectory based on the File_Types mapping.

Enjoy a Cleaner Directory: Once the script completes its operation, your files will be neatly organized into subdirectories.

## File Types Mapping 
The heart of this script is the File_Types dictionary. It associates file extensions with directory names. You can define your own extensions and directories to customize the organization to your liking.

For instance, if you frequently deal with image files, you might want to create a "Pictures" directory for files with ".jpg" and ".png" extensions. Here's an example:

File_Types = {
    ".jpg": "Pictures",
    ".png": "Pictures",
    ".zip": "Archives",
    # Add more extensions and directories as needed
}
Make sure that the directory names you define in the mapping already exist in your target directory. The script will not create new directories; it will move files to existing ones.

## Customization 

Beyond the File_Types dictionary, you can further customize this script to suit your specific needs. Here are some additional customization options:

Change Default Target Directory

If you don't want to organize the Downloads directory or wish to organize a different directory, update the Change_Directory() function with the path to your target directory.
def Change_Directory():
    # Store the current working directory
    Current_Directory = os.getcwd()

    # Change the working directory to your desired path
    os.chdir('/path/to/your/target/directory')

    # Return the path of the new directory
    return os.getcwd()
    
## Modify Directory Creation Behavior

The script currently attempts to create subdirectories if they don't already exist in the target directory. If you want to change this behavior, you can modify the Create_Directory() function. For example, if you prefer not to create directories automatically, remove the os.mkdir(file) line.

## Exclude Specific File Types

If you have specific file types that you want to exclude from organization, you can add conditional statements in the Moving_Files() function to skip those file types. For instance, if you want to skip organizing ".exe" files, you can add:
if extension == ".exe":
    continue  # Skip organizing .exe files

## Advanced Usage

While the script is designed for simplicity, you can explore more advanced use cases:

## Scheduled Execution

You can schedule the script to run at specific intervals using tools like Task Scheduler on Windows or cron jobs on Unix-based systems. This way, your designated directory stays organized automatically.

## Integration with Other Tools

You can integrate this script into more extensive automation workflows or scripts. For example, you might want to combine it with a backup script to organize and back up files simultaneously.

## Error Handling

The script includes basic error handling to ensure it runs smoothly. If the subdirectories already exist, it will ignore the error and proceed with organizing the files. You can customize error handling further to fit your requirements.

##Contributing

If you'd like to contribute to this project, feel free to fork it, make improvements, and submit a pull request. Contributions such as additional features, better error handling, or improved documentation are welcome.

## License

This script is provided under the MIT License. You can find the full license details in the LICENSE file.
By organizing your files efficiently, this script can save you time and reduce the frustration of navigating cluttered directories. Feel free to adapt it to your specific needs, and don't hesitate to contribute to its development. Happy organizing!

