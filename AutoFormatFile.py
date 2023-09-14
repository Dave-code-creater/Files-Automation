import os
import shutil

# Define a mapping of file extensions to directory names
File_Types = {
    ".jpg": "Picture",
    ".zip": "Many Files",
    ".exe": "Execution Files",
    ".txt": "Plain Text",
    ".docx": "Word",
    ".pdf": "Document",
    ".mp4": "Video",
    ".doc": "Word",
    ".mp3": "Audio",
    ".png": "Picture",
    ".pptx": "Presentation",
    ".jpeg": "Picture",
    ".rar" : "Many Files",
    ".gz" : "Many Files",
    ".MOV" : "Video"
}

# Function to change the current working directory to a specific location
def Change_Directory():
    # Store the current working directory
    Current_Directory = os.getcwd()

    # Change the working directory to 'C:/Users/Admin/Downloads'
    os.chdir('C:/Users/Admin/Downloads')

    # Return the path of the new directory
    return os.getcwd()

# Function to list all files in the current directory
def List_All_Files():
    Files = []
    file_in_directory = os.listdir()
    for file in file_in_directory:
        Files.append(file)
    return Files

# Function to create subdirectories based on the File_Types dictionary
def Create_Directory(Directory):
    for file in File_Types.values():
        # Create a subdirectory in the specified directory
        os.mkdir(file)

# Function to move files to their respective subdirectories
def Moving_Files(Directory):
    for file in os.listdir(Directory):
        # Get the file extension (including the dot)
        extension = os.path.splitext(file)[1]

        # Check if the extension is in the File_Types dictionary
        if extension in File_Types:
            # Get the destination directory for the current extension
            destination_directory = File_Types[extension]

            # Create the full path to the source file and the destination path
            source_path = os.path.join(Directory, file)
            new_path = os.path.join(destination_directory, file)

            # Move the file to the destination directory
            shutil.move(source_path, new_path)
        else:
            # If the extension is not in the dictionary, continue to the next file
            continue

# Entry point of the script
if __name__ == "__main__":
    # Change the working directory and store it
    Directory = Change_Directory()

    # Get a list of all files in the current directory
    files = List_All_Files()

    # Try to create subdirectories (ignore if they already exist)
    try:
        Create_Directory(Directory)
    except:
        pass

    # Move files to their respective subdirectories based on their extensions
    Moving_Files(Directory)
