"""
Folder Inspector CLI Tool

Analyzes a folder and reports:
- Total file count
- Breakdown by extension
- Largest file
- Most recently modified file
- Saves JSON report with timestamp

Usage:
    python folder_inspector.py <folder_path>
"""

import os
import sys
import json
from datetime import datetime

# Import from our own package!
from file_utils import generate_timestamped_filename, get_iso_date


def validate_input():
    """
    Validate command-line arguments and return the folder path.
    Exits with error code 1 if validation fails.
    
    Returns:
        str: The validated folder path
    """
    if len(sys.argv)<2:
        print("❌ Error: Please provide a folder path")
        print(f"Usage: python {sys.argv[0]} <folder_path>")
        sys.exit(1)
    folder_path=sys.argv[1]
    if not os.path.isdir(folder_path):
        print(f"❌ Error: '{folder_path}' is not a valid folder")
        sys.exit(1)

    return folder_path


def format_file_size(size_bytes):
    """
    Convert bytes to human-readable format.
    
    Examples:
        500 → "500 B"
        2048 → "2.0 KB"
        2500000 → "2.4 MB"
    
    Parameters:
        size_bytes (int): File size in bytes
    
    Returns:
        str: Human-readable size string
    """
    if size_bytes<1024:
        return f"{size_bytes} B"
    elif size_bytes<(1024*1024):
        kb=size_bytes/1024
        return f"{kb:.1f} KB"
    elif size_bytes<(1024*1024*1024):
        mb=size_bytes/(1024*1024)
        return f"{mb:.1f} MB"
    else:
        gb=size_bytes/(1024*1024*1024)
        return f"{gb:.1f} GB"


def inspect_folder(folder_path):
    """
    Inspect a folder and gather statistics.
    
    Parameters:
        folder_path (str): Path to the folder to inspect
    
    Returns:
        dict: Statistics including total_files, by_extension, 
              largest_file, most_recent_file
    """
    total_files = 0
    by_extension = {}
    largest_size = 0
    largest_file = None
    most_recent_time = 0
    most_recent_file = None

    for item in os.listdir(folder_path):
        full_path=os.path.join(folder_path, item)
        if not os.path.isfile(full_path):
            continue
        total_files+=1
        extension=os.path.splitext(item)[1].lower()
        by_extension[extension]=by_extension.get(extension,0) + 1

        size = os.path.getsize(full_path)
        if size > largest_size:
            largest_size = size
            largest_file = item
        
        modified_time = os.path.getmtime(full_path)
        if modified_time > most_recent_time:
            most_recent_time = modified_time
            most_recent_file = item

    return {
        "total_files": total_files,
        "by_extension": by_extension,
        "largest_file": {
            "name": largest_file,
            "size_bytes": largest_size
        } if largest_file else None,
        "most_recent_file":{
            "name": most_recent_file,
            "modified_timestamp": most_recent_time
        } if most_recent_file else None
    }    

def print_report(stats, folder_path):
    """
    Print the inspection report to the console in a friendly format.
    
    Parameters:
        stats (dict): Statistics from inspect_folder()
        folder_path (str): The folder that was inspected
    """
    print("📁 Folder Inspector Report")
    print("==========================")
    print(f"Folder: {folder_path}")
    print(f"Total files: {stats['total_files']}")
    print("Breakdown by extension:")
    extn=stats["by_extension"]
    for ext,num in extn.items():
        print(f"    {ext}: {num} files")
    if stats["largest_file"] is None:
        print("No files Found")
        return
    else:
        file_info=stats["largest_file"]
        file_size=format_file_size(file_info['size_bytes'])
        print("Largest file:")
        print(f"{file_info["name"]} ({file_size})")
    recent_info=stats["most_recent_file"]
    modified_dt=datetime.fromtimestamp(recent_info["modified_timestamp"])
    modified_str = modified_dt.strftime("%Y-%m-%d %H:%M:%S")
    print("Most recently modified:")
    print(f"{recent_info["name"]} ({modified_str})")



def save_report(stats, folder_path):
    """
    Save the report as a timestamped JSON file.
    
    Parameters:
        stats (dict): Statistics from inspect_folder()
        folder_path (str): The folder that was inspected
    
    Returns:
        str: The filename of the saved report
    """
    filename=generate_timestamped_filename("folder_report",".json")
    report ={
        "folder_path": folder_path,
        "generated_at": get_iso_date(),
        "stats": stats
    }
    try:
        with open(filename,"w") as f:
            json.dump(report, f,indent=2)
    except IOError as e:
        print(f"❌ Failed to save report: {e}")
        return None

    return filename


def main():
    """Orchestrate the inspection workflow."""
    # 1. Validate input
    folder_path = validate_input()
    
    # 2. Inspect the folder
    print(f"\n🔍 Inspecting: {folder_path}\n")
    stats = inspect_folder(folder_path)
    
    # 3. Print report to console
    print_report(stats, folder_path)
    
    # 4. Save report as JSON
    report_filename = save_report(stats, folder_path)
    print(f"\n📄 Report saved: {report_filename}")


if __name__ == "__main__":
    main()