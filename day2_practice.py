name = str(input("Enter Name: "))
age = int(input("Enter Age: "))
fav_lang = str(input("Enter fav programming Language: "))

birth_year = 2025 - age
print(f"Hi {name}! You were born around {birth_year}. Great choice with {fav_lang}!")

sentence = str(input("Enter a sentence: "))

print(f"length of sentence: {len(sentence)}")
print(f"Upper Case: {sentence.upper()}")
print(f"lower case: {sentence.lower()}")
print(f"First 5 Charaters: {sentence[0:5]}")
print(f"last 5 Characters: {sentence[-5:]}")
ispython = "python" in sentence.lower()
if ispython is True :
    print(f"python is present in your sentence")
else :
    print(f"python is not present in your sentence")
