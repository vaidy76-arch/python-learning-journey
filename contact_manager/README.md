# 📇 Contact Management System

A command-line application to manage your contacts efficiently, built with Python.

## Features

- ✅ Add new contacts (name, phone, email, address)
- ✅ View all contacts in a formatted table (sorted alphabetically)
- ✅ Search contacts by name (partial match, case-insensitive)
- ✅ Edit contact details (any field)
- ✅ Delete contacts with confirmation
- ✅ Data persistence (auto-save to JSON)
- ✅ Automatic data loading on startup
- ✅ Input validation and error handling
- ✅ Clean, interactive menu interface

## Technologies Used

- Python 3.11+
- JSON for data storage
- datetime module for timestamps
- Modular design with separate function library

## Project Structure

contact_manager/
├── contact_functions.py  
├── main.py              
├── contacts.json        
└── README.md           

## How to Run

1. Make sure Python 3.11+ is installed
2. Navigate to the contact_manager folder:
```bash
   cd contact_manager
```
3. Run the program:
```bash
   python main.py
```

## Usage

### Main Menu Options:

Add New Contact     - Create a new contact entry
View All Contacts   - Display all contacts in sorted table
Search Contact      - Find contacts by name (partial match)
Edit Contact        - Update any contact field
Delete Contact      - Remove a contact (with confirmation)
Save & Exit         - Save data and quit application

### Sample Workflow:

Add Contact:

Name: Alice Johnson
Phone: 555-1234
Email: alice@email.com
Address: 123 Main St


View All → See Alice in the list
Search "ali" → Finds Alice
Edit Alice → Change phone to 555-0000
Delete Alice → Confirms and removes
Exit → Data automatically saves to JSON

## Data Storage

Contacts are stored in `contacts.json` with this structure:

```json
[
  {
    "id": 1,
    "name": "Alice Johnson",
    "phone": "555-1234",
    "email": "alice@email.com",
    "address": "123 Main St",
    "groups": [],
    "date": "2024-12-15"
  }
]
```

## Functions Module (`contact_functions.py`)

### Core Functions:

- `load_contacts()` - Load contacts from JSON file
- `save_contacts()` - Save contacts to JSON file
- `get_next_id()` - Generate unique contact IDs
- `add_contact()` - Create new contact with duplicate checking
- `view_all_contacts()` - Display formatted table (sorted alphabetically)
- `search_contact()` - Find contacts by name (partial, case-insensitive)
- `edit_contact()` - Update contact fields dynamically
- `delete_contact()` - Remove contact with confirmation

### Key Features:

- **Dynamic field editing**: Automatically adapts to new fields
- **System fields protection**: ID, date, and groups cannot be edited
- **Duplicate prevention**: Checks for existing names before adding
- **Error handling**: Graceful handling of missing files and corrupted data

## Error Handling

The application handles:
- ❌ Missing data file (starts fresh)
- ❌ Corrupted JSON data (notifies user)
- ❌ Invalid user input (validates numbers)
- ❌ Duplicate contacts (prevents creation)
- ❌ Contact not found (appropriate messages)

## Design Decisions

### Why Separate Modules?

- **contact_functions.py**: Pure business logic, reusable functions
- **main.py**: UI/menu logic, user interaction

This separation allows:
- ✅ Easy testing of functions independently
- ✅ Reusable code for other interfaces (GUI, web, etc.)
- ✅ Clear organization and maintainability

### Dynamic Field Detection

```python
SYSTEM_FIELDS = ['id', 'date', 'groups']
editable_fields = [key for key in contact.keys() if key not in SYSTEM_FIELDS]
```

This approach:
- ✅ Automatically includes new fields when added
- ✅ No hardcoded field lists to maintain
- ✅ Future-proof design

## Future Enhancements

Possible improvements:
- [ ] Input validation (phone format, email format)
- [ ] Group management (Family, Work, Friends)
- [ ] Export to CSV
- [ ] Import from CSV
- [ ] Edit/delete multiple contacts
- [ ] Backup/restore functionality
- [ ] Advanced search (by phone, email, etc.)
- [ ] Contact photos
- [ ] GUI interface (Tkinter or web-based)

## What I Learned

This project helped me practice:
- ✅ Functions and modular code organization
- ✅ Working with JSON files (read/write)
- ✅ Exception handling (try/except)
- ✅ List comprehensions and lambda functions
- ✅ String formatting and tables
- ✅ User input validation
- ✅ Dictionary manipulation
- ✅ Code reusability
- ✅ Separation of concerns (UI vs logic)

## Testing

To test the functions independently:

```bash
python contact_functions.py
```

This runs built-in test cases that verify:
- Adding contacts
- Duplicate detection
- Save/load functionality

## Author

Built as capstone project for Week 1 of Python learning journey (Day 7).

**Date:** December 2024  
**Time invested:** ~3-4 hours  
**Lines of code:** ~250+

---

*Second capstone project of Week 1 - Part of my 6-month journey to become a full-stack developer* 🚀

## Acknowledgments

- Built alongside Personal Finance Tracker (first capstone project)
- Demonstrates mastery of Week 1 concepts: variables, control flow, loops, functions, modules, file I/O