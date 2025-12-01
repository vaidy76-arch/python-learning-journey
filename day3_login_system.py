# Day 3 Bonus Challenge 3: Simple Login System

print("=== Login System ===")
print()

# Set correct credentials
correct_username = "user123"
correct_password = "pass456"

# Bonus: Admin credentials
admin_username = "admin"
admin_password = "admin123"

# Get username from user
username = input("Enter username: ")

if username == correct_username:
    password= input("Enter Your Password: ")
    if password==correct_password:
        print (f"✅ Welcome {username}! Access granted.")
    else:
        print ("❌ Incorrect password")
elif username==admin_username:
    password= input("enter Admin password :")
    if password==admin_password:
        print("✅ Hello Admin!! Welcome to Login System")
    else:
        print("❌ Incorrect password")
else:
    print("user does not exists")