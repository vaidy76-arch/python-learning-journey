import sys
import os

# Check if user provided a filename
if len(sys.argv) < 2:
    print("❌ Error: Please provide a filename")
    print(f"Usage: python {sys.argv[0]} <filename>")
    sys.exit(1)

# Get the filename from arguments
filename = sys.argv[1]

# Check if file exists
if os.path.exists(filename):
    print(f"✅ File found: {filename}")
    sys.exit(0)
else:
    print(f"❌ File not found: {filename}")
    sys.exit(1)