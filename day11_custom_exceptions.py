"""
Day 11: Custom Exceptions - Banking System Example
"""

# Step 7: Define custom exceptions

class BankingError(Exception):
    """Base exception for all banking errors"""
    pass

class InsufficientFundsError(BankingError):
    """Raised when account has insufficient funds"""
    pass

class InvalidAmountError(BankingError):
    """Raised when amount is invalid (negative or zero)"""
    pass

class AccountNotFoundError(BankingError):
    """Raised when account doesn't exist"""
    pass


# Banking functions using custom exceptions
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount <= 0:
            raise InvalidAmountError(f"Deposit amount must be positive, got ${amount}")
        
        self.balance += amount
        print(f"✅ Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount <= 0:
            raise InvalidAmountError(f"Withdrawal amount must be positive, got ${amount}")
        
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw ${amount}. Current balance: ${self.balance}"
            )
        
        self.balance -= amount
        print(f"✅ Withdrew ${amount}. New balance: ${self.balance}")


# Test the custom exceptions
print("=== Testing Custom Exceptions ===\n")

account = BankAccount("ACC001", balance=100)

# Test 1: Valid deposit
print("--- Test 1: Valid deposit ---")
try:
    account.deposit(50)
except BankingError as e:
    print(f"❌ {type(e).__name__}: {e}")

# Test 2: Invalid deposit (negative)
print("\n--- Test 2: Invalid deposit (negative amount) ---")
try:
    account.deposit(-20)
except InvalidAmountError as e:
    print(f"❌ {type(e).__name__}: {e}")

# Test 3: Valid withdrawal
print("\n--- Test 3: Valid withdrawal ---")
try:
    account.withdraw(30)
except BankingError as e:
    print(f"❌ {type(e).__name__}: {e}")

# Test 4: Insufficient funds
print("\n--- Test 4: Insufficient funds ---")
try:
    account.withdraw(200)
except InsufficientFundsError as e:
    print(f"❌ {type(e).__name__}: {e}")

# Test 5: Catch all banking errors
print("\n--- Test 5: Multiple operations with general catch ---")
operations = [
    ("deposit", 25),
    ("withdraw", -10),  # Invalid
    ("withdraw", 500),  # Insufficient
    ("deposit", 100),
]

for operation, amount in operations:
    try:
        if operation == "deposit":
            account.deposit(amount)
        else:
            account.withdraw(amount)
    except BankingError as e:
        # Catches ALL banking errors (parent class!)
        print(f"❌ {type(e).__name__}: {e}")

print(f"\n💰 Final balance: ${account.balance}")