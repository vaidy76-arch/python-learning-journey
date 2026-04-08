"""
Contact Management System
Main Program

Manage your contacts with ease!
"""
import contact_functions as cf

def display_menu():
    """Display the main menu."""
    print("\n" + "="*60)
    print("📇 CONTACT MANAGEMENT SYSTEM 📇")
    print("="*60)
    print("1.  Add New Contact")
    print("2.  View All Contacts")
    print("3.  Search Contact")
    print("4.  Edit Contact")
    print("5.  Delete Contact")
    print("6.  Save & Exit")
    print("="*60)

def add_contact_menu(contacts):
    """menu for adding a new contact."""
    print("\n-- Add New contact--")

    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address (optional): ")
    result = cf.add_contact(contacts, name, phone, email, address)

    if isinstance(result, dict):  
        print(f"✅ Contact added! ID: {result['id']}")
    else:  # Error message (duplicate)
        print(f"❌ {result}")

def search_contact_menu(contacts):
    """Menu for searching contacts."""
    print("\n--- Search Contact ---")

    if len(contacts)==0:
        print("No contacts Exists!")
        return
    
    search_item=input("Enter name to search: ")
    cf.search_contact(contacts, search_item)

def edit_contact_menu(contacts):
    """Menu for editing a contact."""
    print("\n--- Edit Contact ---")
    
    if len(contacts) == 0:
        print("No contacts exist!")
        return
    
    # show all contacts
    cf.view_all_contacts(contacts)

    try:
        contact_id= int(input("\nEnter contact ID to edit: "))
        cf.edit_contact(contacts, contact_id)
    except ValueError:
        print("❌ Please enter a valid number!")

def delete_contact_menu(contacts):
    """Menu for deleting a contact."""
    print("\n--- Delete Contact ---")
    
    if len(contacts) == 0:
        print("No contacts exist!")
        return
    
    # Show all contacts 
    cf.view_all_contacts(contacts)

    try:
        contact_id=int(input("\nEnter contact ID to delete: "))
        cf.delete_contact(contacts, contact_id)
    except ValueError:
        print("❌ Please enter a valid number!")

def main():
    """Main program loop."""
    print("\n🌟 Welcome to Contact Management System! 🌟")
    
    # Load existing contacts
    contacts = cf.load_contacts()
    print(f"📂 Loaded {len(contacts)} existing contacts.")

    while True:
        display_menu()
        choice = input("\n Choose as Option from above (1-6): ") 

        if choice=="1":
            add_contact_menu(contacts)
        elif choice == "2":
            cf.view_all_contacts(contacts)
        elif choice == "3":
            search_contact_menu(contacts)
        elif choice == "4":
            edit_contact_menu(contacts)
        elif choice =="5":
            delete_contact_menu(contacts)
        elif choice == "6":
            if cf.save_contacts(contacts):
                print("\n💾 Contacts saved successfully!")
            print("👋 Thank you for using Contact Management System!")
            print("📇 Stay organized! 📇")
            break
        else:
            print("❌ Invalid choice! Please enter 1-6.")

if __name__ == "__main__":
    main()