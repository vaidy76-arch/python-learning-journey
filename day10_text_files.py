"""
Day 10: File Operations - Text Files
"""

# Step 2: Writing to a text file

# Create and write to a file
with open("sample.txt", "w") as f:
    f.write("Hello, this is my first file!\n")
    f.write("This is line 2.\n")
    f.write("This is line 3.\n")

print("File created successfully!")

# Step 3: Reading the entire file
print("\n--- Reading entire file ---")
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# Step 4: Different ways to read files

# Method 1: read() - Read entire file as one string
print("\n--- Method 1: read() ---")
with open("sample.txt", "r") as f:
    content = f.read()
    print(f"Type: {type(content)}")
    print(f"Content: {content}")

# Method 2: readlines() - Read as list of lines
print("\n--- Method 2: readlines() ---")
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(f"Type: {type(lines)}")
    print(f"Number of lines: {len(lines)}")
    print(f"Lines: {lines}")

# Method 3: Loop line by line (memory efficient!)
print("\n--- Method 3: Loop line by line ---")
with open("sample.txt", "r") as f:
    for line_number, line in enumerate(f, 1):
        print(f"Line {line_number}: {line.strip()}")