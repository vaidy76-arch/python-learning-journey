# Day 5 Practice: Student Grade Manager

students = []  # List of student dictionaries
students_avg =[]
print("=== Student Grade Manager ===")
print()

# Add 3-5 students with their grades
# Each student: {"name": "Alice", "grades": [85, 90, 78]}

# Your tasks:
# 1. Add at least 3 students
students.append({"name": "Alice", "grades": [85, 90, 78]})
students.append({"name": "Vaidy", "grades": [92, 88, 70]})
students.append({"name": "Pavi", "grades": [99, 95, 82]})
# 2. Calculate and print each student's average
for student in students:
    grades=student["grades"]
    # Calculate average
    average = sum(grades) / len(grades)
    
    # Print result
    print(f"{student['name']}'s average: {average:.2f}")
    students_avg.append((student["name"],average))


# 3. Find the student with highest average
best=max(students_avg,key=lambda X:X[1])
print(f"Highest average:{best[0]} with {best[1]:.2f}")
# 4. Find the student with lowest average
worst=min(students_avg,key=lambda X:X[1])
print(f"Lowest Average:{worst[0]} with {worst[1]:.2f}")
# 5. Print all students sorted by average (highest first)
sorted_students=sorted(students_avg,key=lambda X:X[1],reverse=True)
print("\nStudents ranked by average:")
for rank, (name, avg) in enumerate(sorted_students, 1):
    print(f"{rank}. {name}: {avg:.2f}")
# 6. Use list comprehensions where possible!