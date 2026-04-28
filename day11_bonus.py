"""
Day 11 Bonus Challenge: Password Strength Validator
"""

# Common weak passwords
COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty",
    "abc123", "password123", "admin", "letmein",
    "welcome", "monkey", "dragon", "master"
]

# Step 1: Define custom exceptions
class PasswordError(Exception):
    """Base exception for password validation"""
    pass

class PasswordTooShortError(PasswordError):
    """Raised when Password Too Short"""

class PasswordTooWeakError(PasswordError):
    """raised when password is too weak"""

class PasswordCommonError(PasswordError):
    """Raised when common password is used"""


# Step 2: Validation function
def validate_password(password):
    """
    Validate password meets all security requirements.
    
    Args:
        password: String password to validate
        
    Returns:
        str: The valid password
        
    Raises:
        PasswordTooShortError: If password < 8 characters
        PasswordTooWeakError: If missing required character types
        PasswordCommonError: If password is in common list
    """
    password=password.strip()

    if not password:
        raise PasswordTooShortError("Passwrod Cannot be empty")
    
    if len(password)<8:
        raise PasswordTooShortError(f"Password shoud be 8 characters or more (got {len(password)})")
    
    if password.lower() in COMMON_PASSWORDS:
        raise PasswordCommonError("This password is too common. Please choose a different one.")
    
    missing = []

    if not any(c.isupper() for c in password):
        missing.append("uppercase letter (A-Z)")

    if not any(c.islower() for c in password):
        missing.append("lowercase letter (a-z)")

    if not any(c.isdigit() for c in password):
        missing.append("digit (0-9)")
    spl_chars ="!@#$%^&*"
    if not any(c in spl_chars for c in password):
        missing.append("special character (!@#$%^&*)")

    if missing:
        missing_str=",".join(missing)
        raise PasswordTooWeakError(f"Password missing: {missing_str}")
    
    return password

  
    


# Step 3: Password strength function
def get_password_strength(password):
    """
    Calculate password strength.
    
    Returns:
        str: "Weak", "Medium", or "Strong"
    
    Criteria:
        Weak:   8-9 characters, meets minimum requirements
        Medium: 10-12 characters, meets minimum requirements
        Strong: 13+ characters, meets minimum requirements
    """
    password=password.strip()
    length = len(password)
    if length>=13:
        return "Strong"
    elif length >=10:
        return "Medium"
    else:
        return "Weak"


# Step 4: Interactive password setter
def set_password_interactive(max_attempts=3):
    """
    Interactive password setting with retry logic.

    Args:
        max_attempts: Maximum number of attempts (default 3)
        
    Returns:
        str: Valid password or None if failed
    """
    print("\n" + "="*50)
    print("🔐 PASSWORD SETUP")
    print("="*50)
    print("\nPassword Requirements:")
    print("  • At least 8 characters long")
    print("  • Contains uppercase letter (A-Z)")
    print("  • Contains lowercase letter (a-z)")
    print("  • Contains digit (0-9)")
    print("  • Contains special character (!@#$%^&*)")
    print("  • Not a common password\n")
    
    attempts=0
    while attempts<max_attempts:
        attempts += 1
        try:
            password=input("\nEnter password: ")
            validate_password(password)
            strength = get_password_strength(password)
            print(f"✅ Password accepted!")
            print(f"💪 Strength: {strength}\n")
            return password
        except PasswordError as e:
            print(f"❌ {type(e).__name__}: {e}")
            if attempts < max_attempts:
                retry = input("Try again? (y/n): ").lower().strip()
                if retry != 'y':
                    print("Password setup cancelled.")
                    return None
            else:
                print(f"\n❌ Maximum attempts ({max_attempts}) reached.")
                return None


# Test your code
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Run automated tests
        print("=== Password Validator Tests ===\n")
        # ... your existing tests ...
        
    else:
        # Run interactive mode
        print("💡 Tip: Run 'python day11_bonus.py test' for automated tests\n")
        password = set_password_interactive()
        
        if password:
            print("="*50)
            print("✅ Password set successfully!")
            print("="*50)
        else:
            print("="*50)
            print("❌ Password setup failed")
            print("="*50)
