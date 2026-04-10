"""
Personal Finance Tracker
Main Program

Track your income and expenses with ease!
"""

import finance_functions as ff


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("💰 PERSONAL FINANCE TRACKER 💰")
    print("="*50)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View All Transactions")
    print("4. View by Category")
    print("5. View Balance & Summary")
    print("6. View All Categories")
    print("7. Save & Exit")
    print("="*50)


def add_income_menu(transactions):
    """Menu for adding income."""
    print("\n--- Add Income ---")
    
    try:
        amount = float(input("Amount: $"))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return
        
        category = input("Category (Salary/Freelance/Other): ")
        description = input("Description: ")
        
        transaction = ff.add_transaction(transactions, "income", amount, category, description)
        print(f"✅ Income added! ID: {transaction['id']}")
        
    except ValueError:
        print("❌ Invalid amount! Please enter a number.")


def add_expense_menu(transactions):
    """Menu for adding expense."""
    print("\n--- Add Expense ---")
    
    try:
        amount = float(input("Amount: $"))
        if amount <= 0:
            print("❌ Amount must be positive!")
            return
        
        category = input("Category (Food/Rent/Transport/Bills/Other): ")
        description = input("Description: ")
        
        transaction = ff.add_transaction(transactions, "expense", amount, category, description)
        print(f"✅ Expense added! ID: {transaction['id']}")
        
    except ValueError:
        print("❌ Invalid amount! Please enter a number.")


def view_all_transactions(transactions):
    """Display all transactions."""
    print("\n--- All Transactions ---")
    
    if len(transactions) == 0:
        print("No transactions yet!")
        return
    
    print(f"\n{'ID':<5} {'Type':<10} {'Amount':<12} {'Category':<15} {'Description':<20} {'Date'}")
    print("-" * 80)
    
    for t in transactions:
        trans_type = t['type'].upper()
        symbol = "+" if t['type'] == 'income' else "-"
        
        print(f"{t['id']:<5} {trans_type:<10} {symbol}${t['amount']:<10.2f} {t['category']:<15} {t['description']:<20} {t['date']}")
    
    print("-" * 80)
    print(f"Total Transactions: {len(transactions)}")


def view_by_category_menu(transactions):
    """View transactions filtered by category."""
    print("\n--- View by Category ---")
    
    if len(transactions) == 0:
        print("No transactions yet!")
        return
    
    # Show available categories
    categories = ff.get_all_categories(transactions)
    print("\nAvailable Categories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")
    
    category = input("\nEnter category name: ")
    
    filtered = ff.get_transactions_by_category(transactions, category)
    
    if len(filtered) == 0:
        print(f"No transactions found for category: {category}")
        return
    
    print(f"\n--- Transactions in '{category}' ---")
    print(f"{'ID':<5} {'Type':<10} {'Amount':<12} {'Description':<20} {'Date'}")
    print("-" * 70)
    
    total = 0
    for t in filtered:
        trans_type = t['type'].upper()
        symbol = "+" if t['type'] == 'income' else "-"
        amount_signed = t['amount'] if t['type'] == 'income' else -t['amount']
        total += amount_signed
        
        print(f"{t['id']:<5} {trans_type:<10} {symbol}${t['amount']:<10.2f} {t['description']:<20} {t['date']}")
    
    print("-" * 70)
    print(f"Category Total: ${total:.2f}")


def view_summary(transactions):
    """Display financial summary."""
    print("\n" + "="*50)
    print("💵 FINANCIAL SUMMARY 💵")
    print("="*50)
    
    if len(transactions) == 0:
        print("No transactions yet!")
        return
    
    income, expenses, balance = ff.calculate_balance(transactions)
    
    print(f"\n{'Total Income:':<20} ${income:,.2f}")
    print(f"{'Total Expenses:':<20} ${expenses:,.2f}")
    print("-" * 50)
    print(f"{'Current Balance:':<20} ${balance:,.2f}")
    
    if balance > 0:
        print("✅ You're in the green!")
    elif balance < 0:
        print("⚠️  Warning: You're spending more than earning!")
    else:
        print("Balance is zero.")
    
    print("\n--- Breakdown by Category ---")
    categories = ff.get_all_categories(transactions)
    
    for category in categories:
        cat_trans = ff.get_transactions_by_category(transactions, category)
        cat_total = sum(t['amount'] if t['type'] == 'income' else -t['amount'] 
                       for t in cat_trans)
        cat_type = "INCOME" if cat_total > 0 else "EXPENSE"
        print(f"  {category:<20} ${abs(cat_total):>10,.2f} ({cat_type})")
    
    print("="*50)


def view_all_categories(transactions):
    """Display all categories."""
    print("\n--- All Categories ---")
    
    if len(transactions) == 0:
        print("No transactions yet!")
        return
    
    categories = ff.get_all_categories(transactions)
    
    print(f"\nTotal Categories: {len(categories)}")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")


def main():
    """Main program loop."""
    print("\n🌟 Welcome to Personal Finance Tracker! 🌟")
    
    # Load existing transactions
    transactions = ff.load_transactions()
    print(f"Loaded {len(transactions)} existing transactions.")
    
    while True:
        display_menu()
        choice = input("\nChoose option (1-7): ")
        
        if choice == "1":
            add_income_menu(transactions)
        
        elif choice == "2":
            add_expense_menu(transactions)
        
        elif choice == "3":
            view_all_transactions(transactions)
        
        elif choice == "4":
            view_by_category_menu(transactions)
        
        elif choice == "5":
            view_summary(transactions)
        
        elif choice == "6":
            view_all_categories(transactions)
        
        elif choice == "7":
            # Save and exit
            if ff.save_transactions(transactions):
                print("\n💾 Data saved successfully!")
            print("👋 Thank you for using Finance Tracker!")
            print("💰 Stay financially healthy! 💰")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-7.")


if __name__ == "__main__":
    main()