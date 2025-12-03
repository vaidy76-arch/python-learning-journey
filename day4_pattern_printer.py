# Day 4 Bonus Challenge 1: Pattern Printer

print("=== Pattern Printer ===")
print()

# Pattern 1: Right triangle
print("Pattern 1: Right Triangle")
rows = 5
for i in range(1, rows + 1):
    # Your code here - print i stars on each row
    print("*"*i)

print()

# Pattern 2: Inverted triangle
print("Pattern 2: Inverted Triangle")
rows=5
for i in range(rows,0,-1):
    print("*"*i)
# Your code here

print()

# Pattern 3: Pyramid
print("Pattern 3: Pyramid")
# Your code here - this one is tricky!
# Hint: you need spaces before the stars

rows =5
for  i in range(1,rows+1):
    space=rows-i
    star=2*i-1
    print(" "*space + "*" *star)

print()

# Pattern 4: Number pyramid
print("Pattern 4: Number Pyramid")
# Print numbers instead of stars
rows=5
for i in range(1,rows+1):
    line=""
    for j in range(1,i+1):
        line+=str(j)
    print(line)

