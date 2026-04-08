"""
Contacts Manager Functions Module

Consists of all Core Functions required for managing contacts.
"""

import json
from datetime import datetime

SYSTEM_FIELDS = ['id', 'date', 'groups']
def load_contacts(filename="contacts.json"):
    """
    Load contacts from JSON file.
    
    Returns:
        list: List of contacts dictionaries
    """
    try:
        with open(filename,"r") as f:
               return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Corrupted File")
        return []

def save_contacts(contacts,filename="contacts.json"):
    """Save contacts to JSON file.
     
     Parameters:
        contacts (list): List of contacts dictonaries
        filename (str): filename where contacts need to be stored
    """
    try:
        with open(filename,"w") as f:
            json.dump(contacts,f,indent=2)
            return True
    except Exception as e:
        print(f"error Saving: {e}")
        return False
def get_next_id(contacts):
    """
    Get the next available Contact ID.
    
    Parameters:
        Contacts (list): List of existing contacts
    
    Returns:
        int: Next ID number
    """
    if len(contacts)==0:
        return 1
    else:
        return max(t["id"] for t in contacts) + 1

def add_contact(contacts,name,phone,email,address=""):
    """
    Add a new contact.
    
    Parameters:
        contacts (list): List of contacts
        name (str): Name of contact
        phone (str): phone number
        email (str): email id
        address (str): contact address
    
    Returns:
        dict: The created contact
    """
    for existing_contact in contacts:
        if existing_contact['name'].lower() == name.lower():
            return "Contact already exists! Please edit existing contact or add new contact with different name"
        
    contact={
        "id": get_next_id(contacts),
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "groups": [],
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    contacts.append(contact)
    return contact

def view_all_contacts(contacts):
    """Display all contacts in a formatted table."""

    if len(contacts)==0:
        print("No contacts exist!")
        return
    
    sorted_contacts = sorted(contacts, key=lambda c:c['name'])
    print("\n" + "="*90)
    print(f"{'ID':<5} {'Name':<20} {'Phone':<15} {'Email':<25} {'Address'}")
    print("-"*90)

    for contact in sorted_contacts:
        print(f"{contact['id']:<5} {contact['name']:<20} {contact['phone']:<15} {contact['email']:<25} {contact.get('address', '')}")
    print("-"*90)
    print(f"Total Contacts: {len(sorted_contacts)}")

def search_contact(contacts, name):
    """
    search contacts by name
    
    Paramets:
        contacts(list): list of contacts
        name(str): name to looks for
    
    """
    results=[c for c in contacts if name.lower() in c['name'].lower()]
    if len(results)==0:
        print("No contacts Found!")
        return
    sorted_results=sorted(results,key=lambda c:c['name'])
    print("\n" + "="*90)
    print(f"{'ID':<5} {'Name':<20} {'Phone':<15} {'Email':<25} {'Address'}")
    print("-"*90)
    for result in sorted_results:
        print(f"{result['id']:<5} {result['name']:<20} {result['phone']:<15} {result['email']:<25} {result.get('address', '')}")
    print("-"*90)
    print(f"No. of contacts found: {len(sorted_results)}")

def edit_contact(contacts,contact_id):
    """
    Edit an existing contact
    
    Parameters:
        contacts (list): list of contacts
        contact_id (int): ID of contact to edit
    """
    for contact in contacts:
        if contact['id']==contact_id:
            print(f"{contact_id}'s Current Details ")
            print("\n--- Current Contact Details ---")
            editable_fields = [key for key in contact.keys() if key not in SYSTEM_FIELDS]
            for index, field in enumerate(editable_fields, 1):
                print(f"{index}. {field.capitalize()}: {contact[field]}")
            print(f"{len(editable_fields) + 1}. Cancel")
            try:
                choice=int(input("\n Enter your choice to edit:-"))
                if 1<=choice<=len(editable_fields):
                    edit_field= editable_fields[choice-1]
                    new_value=input(f"Enter new value for {edit_field}:")
                    contact[edit_field]=new_value
                    print(f"✅ {edit_field.capitalize()} updated!")
                elif choice==len(editable_fields)+1:
                    print(f"Edit Cancelled")
                else:
                    print("Invalid Choice!!")
            except ValueError:
                print("Please enter a number!")
            break
    else:
        print("Contact not found!")
        return
def delete_contact(contacts,contact_id):
    """
    Delete a contact by ID
    
    Parameters:
        contacts (list): list of contacts
        contact_id (int): ID of contact to delete
    
    Returns:
        bool: True if deleted, False if not found/cancelled
    """
    contact = None
    for c in contacts:
        if c['id'] == contact_id:
            contact=c
            break

    if contact is None:
        print("❌ Contact not found!")
        return False
    else:
        # Show what will be deleted
        print("\n--- Contact to Delete ---")
        print(f"ID: {contact['id']}")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")

        # Ask for confirmation
        confirm = input("\n⚠️  Are you sure you want to delete this contact? (yes/no): ")
        if confirm.lower()=="yes":
            contacts.remove(contact)
            print(f"✅ Contact '{contact['name']}' deleted!")
            return True
        else:
            print("❌ Deletion cancelled")
            return False
        

if __name__ == "__main__":
    print("Testing Contact Functions...")
    
    test_contacts = []
    
    # Add contacts
    add_contact(test_contacts, "Alice", "555-1234", "alice@email.com", "123 Main St")
    add_contact(test_contacts, "Bob", "555-5678", "bob@email.com")
    add_contact(test_contacts, "Charlie", "555-9999", "charlie@email.com")
    
    print("\n--- Before Delete ---")
    view_all_contacts(test_contacts)
    
    print("\n--- Testing Delete ---")
    delete_contact(test_contacts, 2)  # Delete Bob
    
    print("\n--- After Delete ---")
    view_all_contacts(test_contacts)  # Should show Alice and Charlie only
