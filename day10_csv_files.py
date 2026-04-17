"""
Day 10: File Operations - CSV Files
"""

import csv

# Step 6: Writing to a CSV file

# Sales data
sales_data = [
    ["date", "product", "quantity", "revenue"],
    ["2024-01-01", "Laptop", 5, 5000],
    ["2024-01-02", "Mouse", 50, 1250],
    ["2024-01-03", "Keyboard", 30, 2250],
    ["2024-01-04", "Monitor", 10, 3000]
]

# Write to CSV file
with open("sales.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sales_data)

print("CSV file created successfully!")


# Step 7: Reading CSV files

# Method 1: csv.reader (returns lists)
print("\n--- Method 1: csv.reader (returns lists) ---")
with open("sales.csv", "r") as f:
    reader = csv.reader(f)
    
    for row in reader:
        print(row)

# Method 2: csv.DictReader (returns dictionaries - BETTER!)
print("\n--- Method 2: csv.DictReader (returns dictionaries) ---")
with open("sales.csv", "r") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        print(row)
        print(f"  Product: {row['product']}, Revenue: ${row['revenue']}")

print("\n--- Practical: Display Column Names ---")
with open("sales.csv", "r") as f:
    reader = csv.DictReader(f)
    
    print("Available columns:")
    for i, column in enumerate(reader.fieldnames, 1):
        print(f"  {i}. {column}")
    
    print("\nData:")
    for row in reader:
        # Now process the data
        print(f"{row['product']}: ${row['revenue']}")

# Step 8: Writing CSV with DictWriter

print("\n--- Writing CSV with DictWriter ---")

# Sales data as list of dictionaries
sales_dict_data = [
    {"date": "2024-01-05", "product": "Headphones", "quantity": 25, "revenue": 2500},
    {"date": "2024-01-06", "product": "Webcam", "quantity": 15, "revenue": 1500},
    {"date": "2024-01-07", "product": "USB Cable", "quantity": 100, "revenue": 500}
]

# Write to CSV using DictWriter
with open("sales_dict.csv", "w", newline='') as f:
    # Define the column headers
    fieldnames = ["date", "product", "quantity", "revenue"]
    
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # Write all data rows
    writer.writerows(sales_dict_data)

print("CSV file with DictWriter created successfully!")