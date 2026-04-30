"""
Timestamping utilities.
Functions for generating timestamped filenames and labels.
"""

from datetime import datetime


def generate_timestamped_filename(base_name, extension):
    """
    Generate a filename with the current timestamp embedded.
    
    Parameters:
        base_name (str): The base name (e.g., 'sales_report')
        extension (str): File extension (e.g., '.csv', 'csv')
    
    Returns:
        str: Filename like 'sales_report_2026-04-29_20-54-49.csv'
    """
    # Normalize extension (same pattern as finder.py)
    if not extension.startswith("."):
        extension = "." + extension
    
    # Get current timestamp in filename-safe format
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Build the filename
    return f"{base_name}_{timestamp}{extension}"


def get_iso_date():
    """
    Return today's date in ISO format (YYYY-MM-DD).
    
    Returns:
        str: Date string like '2026-04-29'
    """
    return datetime.now().strftime("%Y-%m-%d")


if __name__ == "__main__":
    # Test both functions
    print("Testing timestamper functions:")
    
    filename = generate_timestamped_filename("sales_report", ".csv")
    print(f"\nGenerated filename: {filename}")
    
    filename2 = generate_timestamped_filename("backup", "json")  # No dot!
    print(f"Without dot: {filename2}")
    
    today = get_iso_date()
    print(f"\nToday (ISO): {today}")