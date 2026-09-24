# Dynamic Phonebook and Contact Directory Manager

contacts = {}

while True:
    print("\n----- PHONEBOOK MENU -----")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contacts[name] = {
            "phone": phone,
            "email": email
        }

        print("Contact added successfully.")

    # View All Contacts
    elif choice == "2":
        if not contacts:
            print("Phonebook is empty.")
        else:
            print("\nAll Contacts:")

            for name, details in contacts.items():
                print("Name:", name)
                print("Phone:", details["phone"])
                print("Email:", details["email"])
                print("--------------------")

    # Search Contact
    elif choice == "3":
        search = input("Enter name to search: ")

        # List comprehension for dynamic lookup
        result = [name for name in contacts.keys()
                  if search.lower() in name.lower()]

        if result:
            for name in result:
                print("\nName:", name)
                print("Phone:", contacts[name]["phone"])
                print("Email:", contacts[name]["email"])
        else:
            print("Contact not found.")

    # Update Contact
    elif choice == "4":
        name = input("Enter name to update: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")

            contacts[name]["phone"] = phone
            contacts[name]["email"] = email

            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    # Delete Contact
    elif choice == "5":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    # Exit
    elif choice == "6":
        print("Exiting Phonebook...")
        break

    else:
        print("Invalid choice. Please try again.")