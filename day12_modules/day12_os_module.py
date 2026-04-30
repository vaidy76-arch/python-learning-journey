import os

current_dir = os.getcwd()
print(f"I am here: {current_dir}")

# List everything in current folder
items = os.listdir(current_dir)
print(f"\nItems in this folder:")
for item in items:
    print(f"  - {item}")

# Check if a file exists
filename = "day12_os_module.py"
file_path = os.path.join(current_dir, filename)

print(f"\nChecking: {file_path}")

if os.path.exists(file_path):
    print(f"✅ Found: {filename}")
else:
    print(f"❌ Not found: {filename}")

# Check something that doesn't exist
fake_file = "imaginary_file.csv"
fake_path = os.path.join(current_dir, fake_file)

if os.path.exists(fake_path):
    print(f"✅ Found: {fake_file}")
else:
    print(f"❌ Not found: {fake_file}")
