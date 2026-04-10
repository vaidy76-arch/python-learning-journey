# 💰 Personal Finance Tracker

A command-line application to track income and expenses, built with Python.

## Features

- ✅ Add income transactions (salary, freelance, etc.)
- ✅ Add expense transactions (rent, food, transport, etc.)
- ✅ View all transactions in a formatted table
- ✅ Filter transactions by category
- ✅ Calculate balance (income - expenses)
- ✅ View financial summary with category breakdown
- ✅ Data persistence (saves to JSON file)
- ✅ Automatic data loading on startup
- ✅ Input validation and error handling

## Technologies Used

- Python 3.11+
- JSON for data storage
- datetime module for timestamps
- Modular design with separate function library

## Project Structure
```
capstone_project/
├── main.py                 # Main program with menu system
├── finance_functions.py    # Core functions module
├── transactions.json       # Data storage (auto-generated)
└── README.md              # This file
```

## How to Run

1. Make sure Python 3.11+ is installed
2. Navigate to the project folder
3. Run the program:
```bash
   python main.py
```

## Usage

### Main Menu Options:

1. **Add Income** - Record money received (salary, freelance, etc.)
2. **Add Expense** - Record money spent (rent, food, bills, etc.)
3. **View All Transactions** - See complete transaction history
4. **View by Category** - Filter transactions by category
5. **View Balance & Summary** - See financial overview with totals
6. **View All Categories** - List all transaction categories
7. **Save & Exit** - Save data and quit application

### Sample Workflow:
```
1. Add Income: $5000 (Salary)
2. Add Expense: $1200 (Rent)
3. Add Expense: $300 (Food)
4. View Balance → See you have $3500 remaining
5. Exit → Data automatically saves
```

## Data Storage

Transactions are stored in `transactions.json` with this structure:
```json
[
  {
    "id": 1,
    "type": "income",
    "amount": 5000.0,
    "category": "Salary",
    "description": "Monthly salary",
    "date": "2024-12-15"
  }
]
```

## Functions Module

`finance_functions.py` contains:
- `load_transactions()` - Load data from JSON
- `save_transactions()` - Save data to JSON
- `add_transaction()` - Create new transaction
- `calculate_balance()` - Calculate financial totals
- `get_transactions_by_category()` - Filter by category
- `get_all_categories()` - Get unique categories

## Error Handling

The app handles:
- Missing data file (starts fresh)
- Corrupted JSON data
- Invalid user input (non-numeric amounts)
- Negative amounts (rejected)
- File save errors

## Future Enhancements

Possible improvements:
- [ ] Edit/delete transactions
- [ ] Date range filtering (monthly/yearly reports)
- [ ] Budget setting and alerts
- [ ] Export to CSV
- [ ] Charts/graphs (with matplotlib)
- [ ] Recurring transactions
- [ ] Multiple currency support

## What I Learned

This project helped me practice:
- Functions and modular code
- Working with JSON files
- Exception handling
- List comprehensions
- Working with dictionaries
- User input validation
- String formatting
- Code organization

## Author

Built as capstone project for Week 1 of Python learning journey.

**Date:** December 2024  
**Time invested:** ~2 hours (Day 7)

---

*Part of my 6-month journey to become a full-stack developer* 🚀