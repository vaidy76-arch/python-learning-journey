# Understanding where Python looks for modules

import sys

print("Python searches for modules in these locations:")
for path in sys.path:
    print(f"  - {path}")
print()

# Your current directory is usually first!
# That's why your my_calculator.py works