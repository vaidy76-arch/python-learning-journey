"""
Day 11: Practice Exercise - User Input Validator
Robust user registration system with custom exceptions
"""

# Step 10: Define custom validation exceptions

class ValidationError(Exception):
    """Base exception for all validation errors"""
    pass

class InvalidAgeError(ValidationError):
    """Raised when age is invalid"""
    pass

class InvalidEmailError(ValidationError):
    """Raised when email format is invalid"""
    pass

class InvalidPhoneError(ValidationError):
    """Raised when phone number is invalid"""
    pass


# Test the exceptions are defined
print("✅ Custom exceptions defined:")
print(f"  - ValidationError (base)")
print(f"  - InvalidAgeError")
print(f"  - InvalidEmailError")
print(f"  - InvalidPhoneError")

# Step 14: Automated test mode

def run_automated_tests():
    """Run automated tests for all validation functions"""
    print("\n" + "="*60)
    print("🧪 AUTOMATED VALIDATION TESTS")
    print("="*60 + "\n")
    
    test_results = {"passed": 0, "failed": 0}
    
    # ========================================
    # Age Validation Tests
    # ========================================
    print("--- Age Validation Tests ---\n")
    
    age_tests = [
        ("25", True, "Valid age"),
        ("18", True, "Minimum valid age"),
        ("fifteen", False, "Not a number"),
        ("17", False, "Under 18"),
        ("150", False, "Unrealistic age"),
        ("-5", False, "Negative age"),
    ]
    
    for test_input, should_pass, description in age_tests:
        try:
            result = validate_age(test_input)
            if should_pass:
                print(f"✅ PASS: {description} - got {result}")
                test_results["passed"] += 1
            else:
                print(f"❌ FAIL: {description} - should have raised error")
                test_results["failed"] += 1
        except InvalidAgeError as e:
            if not should_pass:
                print(f"✅ PASS: {description} - correctly rejected ({e})")
                test_results["passed"] += 1
            else:
                print(f"❌ FAIL: {description} - unexpected error: {e}")
                test_results["failed"] += 1
    
    # ========================================
    # Email Validation Tests
    # ========================================
    print("\n--- Email Validation Tests ---\n")
    
    email_tests = [
        ("john@example.com", True, "Valid email"),
        ("alice@test.co.uk", True, "Valid with subdomain"),
        ("john.example.com", False, "Missing @"),
        ("@example.com", False, "Missing username"),
        ("john@", False, "Missing domain"),
        ("john@@example.com", False, "Multiple @ symbols"),
        ("john@examplecom", False, "Missing dot in domain"),
        ("", False, "Empty email"),
    ]
    
    for test_input, should_pass, description in email_tests:
        try:
            result = validate_email(test_input)
            if should_pass:
                print(f"✅ PASS: {description} - got {result}")
                test_results["passed"] += 1
            else:
                print(f"❌ FAIL: {description} - should have raised error")
                test_results["failed"] += 1
        except InvalidEmailError as e:
            if not should_pass:
                print(f"✅ PASS: {description} - correctly rejected")
                test_results["passed"] += 1
            else:
                print(f"❌ FAIL: {description} - unexpected error: {e}")
                test_results["failed"] += 1
    
    # ========================================
    # Phone Validation Tests
    # ========================================
    print("\n--- Phone Validation Tests ---\n")
    
    phone_tests = [
        ("5551234567", True, "Valid 10-digit phone"),
        ("555-123-4567", True, "Valid with dashes"),
        ("555 123 4567", True, "Valid with spaces"),
        ("123", False, "Too short"),
        ("12345678901", False, "Too long"),
        ("555-CALL-NOW", False, "Contains letters"),
        ("", False, "Empty phone"),
    ]
    
    for test_input, should_pass, description in phone_tests:
        try:
            result = validate_phone(test_input)
            if should_pass:
                print(f"✅ PASS: {description} - got {result}")
                test_results["passed"] += 1
            else:
                print(f"❌ FAIL: {description} - should have raised error")
                test_results["failed"] += 1
        except InvalidPhoneError as e:
            if not should_pass:
                print(f"✅ PASS: {description} - correctly rejected")
                test_results["passed"] += 1
            else:
                print(f"❌ FAIL: {description} - unexpected error: {e}")
                test_results["failed"] += 1
    
    # ========================================
    # Test Summary
    # ========================================
    print("\n" + "="*60)
    print("📊 TEST SUMMARY")
    print("="*60)
    print(f"✅ Passed: {test_results['passed']}")
    print(f"❌ Failed: {test_results['failed']}")
    print(f"📈 Total:  {test_results['passed'] + test_results['failed']}")
    
    if test_results['failed'] == 0:
        print("\n🎉 ALL TESTS PASSED!")
    else:
        print(f"\n⚠️  {test_results['failed']} test(s) failed")
    
    print("="*60 + "\n")

# Step 11: Create validation functions

def validate_age(age_str):
    """
    Validate age input.
    
    Args:
        age_str: String input from user
        
    Returns:
        int: Valid age
        
    Raises:
        InvalidAgeError: If age is invalid
    """
    # Check if it's a number
    try:
        age = int(age_str)
    except ValueError:
        raise InvalidAgeError("Age must be a number")
    
    # Check if 18 or older
    if age < 18:
        raise InvalidAgeError(f"Must be 18 or older (got {age})")
    
    # Check reasonable upper limit
    if age > 120:
        raise InvalidAgeError(f"Age {age} seems unrealistic")
    
    return age


def validate_email(email):
    """
    Validate email format.
    
    Args:
        email: String email address
        
    Returns:
        str: Valid email
        
    Raises:
        InvalidEmailError: If email format is invalid
    """
    # Remove whitespace
    email = email.strip()
    
    # Check if empty
    if not email:
        raise InvalidEmailError("Email cannot be empty")
    
    # Check for @ symbol
    if '@' not in email:
        raise InvalidEmailError("Email must contain '@'")
    
    # Check for . after @
    parts = email.split('@')
    if len(parts) != 2:
        raise InvalidEmailError("Email must have exactly one '@'")
    
    username, domain = parts
    
    if not username:
        raise InvalidEmailError("Email must have username before '@'")
    
    if '.' not in domain:
        raise InvalidEmailError("Email domain must contain '.'")
    
    return email


def validate_phone(phone):
    """
    Validate phone number.
    
    Args:
        phone: String phone number
        
    Returns:
        str: Valid phone number
        
    Raises:
        InvalidPhoneError: If phone is invalid
    """
    # Remove spaces and dashes
    phone = phone.replace(' ', '').replace('-', '')
    
    # Check if empty
    if not phone:
        raise InvalidPhoneError("Phone number cannot be empty")
    
    # Check if all digits
    if not phone.isdigit():
        raise InvalidPhoneError("Phone number must contain only digits")
    
    # Check length (US phone: 10 digits)
    if len(phone) != 10:
        raise InvalidPhoneError(f"Phone must be 10 digits (got {len(phone)})")
    
    return phone


# Test the validation functions
print("\n=== Testing Validation Functions ===\n")

# Test 1: Valid age
print("--- Test 1: Valid age ---")
try:
    age = validate_age("25")
    print(f"✅ Valid age: {age}")
except InvalidAgeError as e:
    print(f"❌ {e}")

# Test 2: Invalid age (not a number)
print("\n--- Test 2: Invalid age (not a number) ---")
try:
    age = validate_age("twenty")
    print(f"✅ Valid age: {age}")
except InvalidAgeError as e:
    print(f"❌ {e}")

# Test 3: Invalid age (too young)
print("\n--- Test 3: Invalid age (too young) ---")
try:
    age = validate_age("15")
    print(f"✅ Valid age: {age}")
except InvalidAgeError as e:
    print(f"❌ {e}")

# Test 4: Valid email
print("\n--- Test 4: Valid email ---")
try:
    email = validate_email("john@example.com")
    print(f"✅ Valid email: {email}")
except InvalidEmailError as e:
    print(f"❌ {e}")

# Test 5: Invalid email (no @)
print("\n--- Test 5: Invalid email (no @) ---")
try:
    email = validate_email("john.example.com")
    print(f"✅ Valid email: {email}")
except InvalidEmailError as e:
    print(f"❌ {e}")

# Test 6: Valid phone
print("\n--- Test 6: Valid phone ---")
try:
    phone = validate_phone("555-123-4567")
    print(f"✅ Valid phone: {phone}")
except InvalidPhoneError as e:
    print(f"❌ {e}")

# Test 7: Invalid phone (letters)
print("\n--- Test 7: Invalid phone (contains letters) ---")
try:
    phone = validate_phone("555-CALL-NOW")
    print(f"✅ Valid phone: {phone}")
except InvalidPhoneError as e:
    print(f"❌ {e}")

    # Step 12: Add retry logic

def get_validated_input(field_name, validator_func, max_attempts=3):
    """
    Get user input with validation and retry logic.
    
    Args:
        field_name: Name of the field (e.g., "age", "email")
        validator_func: Function to validate the input
        max_attempts: Maximum number of attempts allowed
        
    Returns:
        Validated value or None if all attempts failed
    """
    attempts = 0
    
    while attempts < max_attempts:
        attempts += 1
        
        try:
            # Get user input
            user_input = input(f"Enter your {field_name}: ").strip()
            
            # Validate using the provided function
            validated_value = validator_func(user_input)
            
            # Success!
            print(f"✅ {field_name.capitalize()} validated: {validated_value}")
            return validated_value
            
        except ValidationError as e:
            # Validation failed
            print(f"❌ {type(e).__name__}: {e}")
            
            # Check if we have more attempts
            if attempts < max_attempts:
                retry = input("Try again? (y/n): ").lower().strip()
                if retry != 'y':
                    print(f"Skipping {field_name} validation.")
                    return None
            else:
                print(f"Maximum attempts ({max_attempts}) reached for {field_name}.")
                return None
        
        except KeyboardInterrupt:
            # User pressed Ctrl+C
            print("\n\n⚠️  Registration cancelled by user.")
            return None
    
    return None


# Test the retry logic
print("\n" + "="*50)
print("=== Testing Retry Logic ===")
print("="*50 + "\n")

print("Test: You'll be asked for age with retry logic")
print("Try entering invalid values, then a valid one\n")

# Uncomment to test interactively:
age = get_validated_input("age", validate_age)
if age:
    print(f"\nFinal validated age: {age}")
else:
    print("\nAge validation failed or skipped")

# Step 13: Complete registration flow

def register_user():
    """
    Complete user registration with validation and retry logic.
    
    Returns:
        dict: User data if successful, None if failed
    """
    print("\n" + "="*50)
    print("🎯 USER REGISTRATION SYSTEM")
    print("="*50 + "\n")
    
    user_data = {}
    
    # Get name (no validation needed)
    try:
        name = input("Enter your name: ").strip()
        if not name:
            print("❌ Name cannot be empty")
            return None
        user_data['name'] = name
        print(f"✅ Name accepted: {name}\n")
    except KeyboardInterrupt:
        print("\n\n⚠️  Registration cancelled.")
        return None
    
    # Validate age
    print("--- Age Validation ---")
    age = get_validated_input("age", validate_age)
    if age is None:
        print("❌ Registration failed: Age required\n")
        return None
    user_data['age'] = age
    print()
    
    # Validate email
    print("--- Email Validation ---")
    email = get_validated_input("email", validate_email)
    if email is None:
        print("❌ Registration failed: Email required\n")
        return None
    user_data['email'] = email
    print()
    
    # Validate phone
    print("--- Phone Validation ---")
    phone = get_validated_input("phone", validate_phone)
    if phone is None:
        print("❌ Registration failed: Phone required\n")
        return None
    user_data['phone'] = phone
    print()
    
    # Success!
    return user_data


def display_registration_result(user_data):
    """Display the registration result"""
    if user_data:
        print("="*50)
        print("✅ REGISTRATION COMPLETE!")
        print("="*50)
        print(f"Name:  {user_data['name']}")
        print(f"Age:   {user_data['age']}")
        print(f"Email: {user_data['email']}")
        print(f"Phone: {user_data['phone']}")
        print("="*50)
    else:
        print("="*50)
        print("❌ REGISTRATION FAILED")
        print("="*50)


# Main program
if __name__ == "__main__":
    import sys
    
    # Check for test mode
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Run automated tests
        run_automated_tests()
    else:
        # Run interactive registration
        print("💡 Tip: Run 'python day11_practice.py test' for automated tests\n")
        result = register_user()
        display_registration_result(result)