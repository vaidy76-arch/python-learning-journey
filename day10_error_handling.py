import json
def read_json_safe(filename):
    """
    Safely read a JSON file with error handling.
    
    Returns:
        - Dictionary with data if successful
        - None if any error occurs
    """
    try:
        with open(filename,"r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"{filename} file not found!!")
    except json.JSONDecodeError:
        print(f"{filename} is broken json!!")    
    except PermissionError:
        print(f"{filename} not having read permissions!!")
    except Exception as e:
        print(f"Error reading '{filename}': {e}")

# Test cases
print("=== Test 1: Valid file ===")
data = read_json_safe("employees.json")
if data:
    print(f"Success! Company: {data['company']}")
else:
    print("Failed to read file")
print("\n=== Test 2: Missing file ===")
data = read_json_safe("employees1.json")
if data:
    print("✅ Success!")
else:
    print("❌ Failed as expected")

print("\n=== Test 3: Corrupted JSON ===")
with open("broken.json", "w") as f:
    f.write("{invalid json content")

data = read_json_safe("broken.json")
if data:
    print("✅ Success!")
else:
    print("❌ Failed as expected")