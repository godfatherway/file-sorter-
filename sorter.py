import os
import shutil

def sort_files_by_extension(folder_path):
    # Iterate over all items in the folder
    for root, dirs, files in os.walk(folder_path):
        # For each file in the current directory
        for filename in files:
            # Construct the full file path
            file_path = os.path.join(root, filename)
            
            # Get the file extension
            _, extension = os.path.splitext(filename)
            
            # Create a directory with the extension name if it doesn't exist
            extension_folder = os.path.join(folder_path, extension[1:])
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)
            
            # Move the file to the extension folder
            shutil.move(file_path, os.path.join(extension_folder, filename))

# Replace 'folder_path' with the path to your desired folder
folder_path = r'C:\Users\Andrei Fuentes\Desktop\tjmedia\tjt\TJT'

# Call the function to sort files by extension
sort_files_by_extension(folder_path)
