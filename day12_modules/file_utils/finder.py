"""
File finder utilities.
Functions for locating files by extension, pattern, etc.
"""

import os


def find_files_by_extension(folder_path, extension):
    """
    Find all files in a folder with a specific extension.
    
    Parameters:
        folder_path (str): Path to the folder to search
        extension (str): File extension to look for (e.g., '.csv', '.txt')
    
    Returns:
        list: Full paths of matching files. Empty list if folder doesn't exist.
    """
    # Check if folder exists first
    if not os.path.exists(folder_path):
        print(f"⚠️  Folder not found: {folder_path}")
        return []
    
    # Make sure extension starts with a dot
    if not extension.startswith("."):
        extension = "." + extension
    
    # Make extension lowercase for case-insensitive matching
    extension = extension.lower()
    
    # Find matching files
    matching_files = []
    
    for item in os.listdir(folder_path):
        # Build full path
        full_path = os.path.join(folder_path, item)
        
        # Check: is it a file (not a folder)? Does it end with our extension?
        if os.path.isfile(full_path) and item.lower().endswith(extension):
            matching_files.append(full_path)
    
    return matching_files


if __name__ == "__main__":
    # Test the function when run directly
    print("Testing find_files_by_extension:")
    
    # Test with the parent folder (day12_modules)
    py_files = find_files_by_extension("..", ".py")
    print(f"\nFound {len(py_files)} Python files:")
    for f in py_files:
        print(f"  - {f}")