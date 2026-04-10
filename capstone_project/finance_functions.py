"""
Finance Tracker Functions Module

Contains all core functions for the personal finance tracker.
"""

import json
from datetime import datetime


def load_transactions(filename="transactions.json"):
    """
    Load transactions from JSON file.
    
    Returns:
        list: List of transaction dictionaries
    """
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Corrupted data file. Starting fresh.")
        return []


def save_transactions(transactions, filename="transactions.json"):
    """
    Save transactions to JSON file.
    
    Parameters:
        transactions (list): List of transaction dictionaries
        filename (str): Filename to save to
    """
    try:
        with open(filename, "w") as f:
            json.dump(transactions, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving: {e}")
        return False


def get_next_id(transactions):
    """
    Get the next available transaction ID.
    
    Parameters:
        transactions (list): List of existing transactions
    
    Returns:
        int: Next ID number
    """
    if len(transactions) == 0:
        return 1
    return max(t["id"] for t in transactions) + 1


def add_transaction(transactions, trans_type, amount, category, description):
    """
    Add a new transaction.
    
    Parameters:
        transactions (list): List of transactions
        trans_type (str): "income" or "expense"
        amount (float): Transaction amount
        category (str): Category name
        description (str): Transaction description
    
    Returns:
        dict: The created transaction
    """
    transaction = {
        "id": get_next_id(transactions),
        "type": trans_type,
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    transactions.append(transaction)
    return transaction


def calculate_balance(transactions):
    """
    Calculate current balance (total income - total expenses).
    
    Parameters:
        transactions (list): List of transactions
    
    Returns:
        tuple: (total_income, total_expenses, balance)
    """
    total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
    total_expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = total_income - total_expenses
    return total_income, total_expenses, balance


def get_transactions_by_category(transactions, category):
    """
    Get all transactions for a specific category.
    
    Parameters:
        transactions (list): List of transactions
        category (str): Category to filter by
    
    Returns:
        list: Filtered transactions
    """
    return [t for t in transactions if t["category"].lower() == category.lower()]


def get_all_categories(transactions):
    """
    Get list of all unique categories.
    
    Parameters:
        transactions (list): List of transactions
    
    Returns:
        list: List of unique category names
    """
    categories = set(t["category"] for t in transactions)
    return sorted(categories)


if __name__ == "__main__":
    # Test the functions
    print("Testing Finance Functions...")
    
    test_trans = []
    
    # Add test transactions
    add_transaction(test_trans, "income", 5000, "Salary", "Monthly salary")
    add_transaction(test_trans, "expense", 500, "Rent", "Monthly rent")
    add_transaction(test_trans, "expense", 100, "Food", "Groceries")
    
    # Test calculations
    income, expenses, balance = calculate_balance(test_trans)
    print(f"Income: ${income}")
    print(f"Expenses: ${expenses}")
    print(f"Balance: ${balance}")
    
    print("\nAll transactions:")
    for t in test_trans:
        print(f"  {t}")