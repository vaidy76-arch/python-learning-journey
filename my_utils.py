"""
My Utilities Module

Useful helper functions for everyday tasks.
"""

def reverse_string(text):
    """Reverse a string"""
    return text[::-1]

def count_vowels(text):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def is_palindrome(text):
    """Check if text is a palindrome"""
    text = text.lower().replace(" ", "")
    return text == text[::-1]

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    print("Testing utilities...")
    print(reverse_string("Python"))
    print(count_vowels("Hello World"))
    print(is_palindrome("racecar"))