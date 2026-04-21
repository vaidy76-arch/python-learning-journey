"""
Day 10: File Operations - JSON Files
"""

import json

# Step 10: Writing complex JSON data

# Complex nested data structure
employee_data = {
    "company": "TechCorp",
    "employees": [
        {
            "id": 1,
            "name": "Alice Johnson",
            "position": "Developer",
            "salary": 85000,
            "skills": ["Python", "JavaScript", "SQL"],
            "address": {
                "street": "123 Main St",
                "city": "San Antonio",
                "state": "TX"
            }
        },
        {
            "id": 2,
            "name": "Bob Smith",
            "position": "Manager",
            "salary": 95000,
            "skills": ["Leadership", "Project Management"],
            "address": {
                "street": "456 Oak Ave",
                "city": "Austin",
                "state": "TX"
            }
        }
    ],
    "departments": ["Engineering", "HR", "Sales"]
}

# Write to JSON file with pretty formatting
with open("employees.json", "w") as f:
    json.dump(employee_data, f, indent=2)

print("JSON file created successfully!")

# Step 11: Reading JSON data

print("\n--- Reading JSON file ---")
with open("employees.json", "r") as f:
    data = json.load(f)

# Display the entire structure
print(f"Type: {type(data)}")
print(f"Company: {data['company']}")

# Access nested data
print("\n--- Accessing nested data ---")
first_employee = data['employees'][0]
print(f"First employee: {first_employee['name']}")
print(f"Position: {first_employee['position']}")
print(f"City: {first_employee['address']['city']}")
print(f"First skill: {first_employee['skills'][0]}")

# Loop through all employees
print("\n--- All Employees ---")
for employee in data['employees']:
    print(f"\nID: {employee['id']}")
    print(f"Name: {employee['name']}")
    print(f"Position: {employee['position']}")
    print(f"Salary: ${employee['salary']:,}")
    print(f"Skills: {', '.join(employee['skills'])}")
    print(f"Location: {employee['address']['city']}, {employee['address']['state']}")