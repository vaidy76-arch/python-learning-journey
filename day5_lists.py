# Day 5: Lists & Tuples - Deep Dive

print("=== List Basics ===")
print()

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # Lists can hold different types!
empty = []

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")

# Accessing elements (indexing)
print(f"\nFirst fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second fruit: {fruits[1]}")

# List length
print(f"\nNumber of fruits: {len(fruits)}")

# Checking if item exists
print(f"\n'apple' in fruits: {'apple' in fruits}")
print(f"'mango' in fruits: {'mango' in fruits}")

# List Methods - These MODIFY the original list

print("\n=== List Methods ===")
print()

# Starting list
colors = ["red", "blue", "green"]
print(f"Original: {colors}")

# 1. append() - add item to end
colors.append("yellow")
print(f"After append('yellow'): {colors}")

# 2. insert() - add item at specific position
colors.insert(1, "orange")  # Insert at index 1
print(f"After insert(1, 'orange'): {colors}")

# 3. remove() - remove first occurrence of item
colors.remove("blue")
print(f"After remove('blue'): {colors}")

# 4. pop() - remove and return item at index (or last if no index)
last_color = colors.pop()  # Removes last item
print(f"Popped: {last_color}")
print(f"After pop(): {colors}")

second_color = colors.pop(1)  # Remove at index 1
print(f"Popped at index 1: {second_color}")
print(f"After pop(1): {colors}")

# 5. clear() - remove all items
colors_copy = colors.copy()  # Make a copy first
colors_copy.clear()
print(f"After clear(): {colors_copy}")

print()

# Sorting and reversing
numbers = [5, 2, 8, 1, 9, 3]
print(f"Original numbers: {numbers}")

# 6. sort() - sort in place (modifies original)
numbers.sort()
print(f"After sort(): {numbers}")

# 7. reverse() - reverse in place
numbers.reverse()
print(f"After reverse(): {numbers}")

# sorted() and reversed() - return NEW list (don't modify original)
original = [5, 2, 8, 1]
sorted_list = sorted(original)  # Returns new sorted list
print(f"\nOriginal: {original}")
print(f"Sorted (new list): {sorted_list}")

# 8. count() - count occurrences
numbers = [1, 2, 2, 3, 2, 4]
print(f"\nCount of 2 in {numbers}: {numbers.count(2)}")

# 9. index() - find first index of item
print(f"Index of 3: {numbers.index(3)}")

# List Slicing - Extract portions of a list

print("\n=== List Slicing ===")
print()

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10]
print(f"Original: {numbers}")

# Basic slicing: list[start:end] (end not included)
print(f"numbers[2:5]: {numbers[2:5]}")      # [2, 3, 4]
print(f"numbers[:4]: {numbers[:4]}")        # [0, 1, 2, 3] (from start)
print(f"numbers[5:]: {numbers[5:]}")        # [5, 6, 7, 8, 9] (to end)
print(f"numbers[-3:]: {numbers[-3:]}")      # [7, 8, 9] (last 3)

# Step slicing: list[start:end:step]
print(f"numbers[::2]: {numbers[::2]}")      # [0, 2, 4, 6, 8] (every 2nd)
print(f"numbers[1::2]: {numbers[1::2]}")    # [1, 3, 5, 7, 9] (odd numbers)
print(f"numbers[::-1]: {numbers[::-1]}")    # Reverse the list!

# Practical examples
letters = ['a', 'b', 'c', 'd', 'e', 'f','g','h']
print(f"\nLetters: {letters}")
print(f"First 3: {letters[:3]}")
print(f"Last 3: {letters[-3:]}")
print(f"Middle items: {letters[2:4]}")
print(f"Every other: {letters[::2]}")

# List Comprehensions - Create lists in ONE line!

print("\n=== List Comprehensions ===")
print()

# Traditional way - using loop
squares_old = []
for i in range(1, 6):
    squares_old.append(i ** 2)
print(f"Squares (old way): {squares_old}")

# List comprehension way - ONE line!
squares_new = [i ** 2 for i in range(1, 6)]
print(f"Squares (comprehension): {squares_new}")

# More examples
# 1. Double all numbers
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(f"\nOriginal: {numbers}")
print(f"Doubled: {doubled}")

# 2. Convert to uppercase
fruits = ["apple", "banana", "cherry"]
upper_fruits = [fruit.upper() for fruit in fruits]
print(f"\nFruits: {fruits}")
print(f"Uppercase: {upper_fruits}")

# 3. With condition (filter)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]
print(f"\nNumbers: {numbers}")
print(f"Even numbers: {evens}")

# 4. More complex
words = ["hello", "world", "python", "code"]
lengths = [len(word) for word in words]
print(f"\nWords: {words}")
print(f"Lengths: {lengths}")

# 5. Nested - first letter of each word
sentence = "the quick brown fox"
first_letters = [word[0] for word in sentence.split()]
print(f"\nSentence: {sentence}")
print(f"First letters: {first_letters}")


# Tuples - Like lists but IMMUTABLE (can't be changed)

print("\n=== Tuples ===")
print()

# Creating tuples - use parentheses ()
coordinates = (10, 20)
colors = ("red", "green", "blue")
single = (42,)  # Note the comma for single item tuple!

print(f"Coordinates: {coordinates}")
print(f"Colors: {colors}")
print(f"Single item tuple: {single}")

# Accessing works like lists
print(f"\nFirst coordinate: {coordinates[0]}")
print(f"Last color: {colors[-1]}")

# Can't modify tuples!
# colors[0] = "yellow"  # This would ERROR!

# But you can do:
print(f"\nLength: {len(colors)}")
print(f"Count of 'red': {colors.count('red')}")
print(f"Index of 'blue': {colors.index('blue')}")

# Tuple unpacking (very useful!)
x, y = coordinates
print(f"\nx = {x}, y = {y}")

name, age, city = ("Alice", 25, "NYC")
print(f"Name: {name}, Age: {age}, City: {city}")

# When to use tuples vs lists?
# Lists: When data will change (add/remove items)
# Tuples: When data should NOT change (coordinates, RGB colors, etc.)

print("\n=== List vs Tuple ===")
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

my_list.append(4)  # ✅ Works
print(f"List after append: {my_list}")

# my_tuple.append(4)  # ❌ ERROR - tuples don't have append!
print(f"Tuple unchanged: {my_tuple}")