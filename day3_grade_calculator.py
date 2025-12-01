# Day 3 Bonus Challenge 2: Grade Calculator

print("=== Grade Calculator ===")
print()

score = int(input("Enter student score (0-100): "))

if score < 0 or score >100:
    print ("Invalid Score! Must be between 0 and 100")
else:
    if score >=90 :
        print("Grade: A - Excellent!")
    elif score >=80:
        print("Grade: B - Very Good")
    elif score >=70:
        print("Grade: C - Good")
    elif score >=60:
        print("Grade: D - Average")
    else:
        print("Grade: F - Poor")

