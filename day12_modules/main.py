"""
Demo script using the file_utils package.
Finds all Python files in this folder and shows
what their backup filenames would be.
"""

# Notice: we don't need to know about 'finder' or 'timestamper' modules!
# The package's __init__.py exposes these directly.
from file_utils import find_files_by_extension, generate_timestamped_filename, get_iso_date


def main():
    print(f"📅 Today is: {get_iso_date()}")
    print(f"\n🔍 Searching for Python files in current folder...\n")
    
    # Find all .py files in the current folder
    py_files = find_files_by_extension(".", ".py")
    
    if not py_files:
        print("No Python files found.")
        return
    
    print(f"Found {len(py_files)} Python file(s):\n")
    
    # For each file, show what its timestamped backup name would be
    for py_file in py_files:
        # Get just the base name without path or extension
        # Example: '.\day12_os_module.py' → 'day12_os_module'
        import os
        base_name = os.path.splitext(os.path.basename(py_file))[0]
        
        # Generate a backup filename
        backup_name = generate_timestamped_filename(base_name + "_backup", ".py")
        
        print(f"  📄 {py_file}")
        print(f"     → Backup would be: {backup_name}\n")


if __name__ == "__main__":
    main()