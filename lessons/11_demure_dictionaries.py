# Define dictionary to store contact info
contacts = dict()

# Start printing menu
print()
print("Welcome to the Contact Manager!")

# Loop until user chooses to exit
while True:
    # Define options function to run every time after choosing an action
    def options():
        # Print options
        print()
        print("Choose an option:")
        print("1. Add a contact")
        print("2. Remove a contact")
        print("3. List contacts")
        print("4. Exit the program")
        print()

    options()

    # User inputs choice
    option = int(input("Enter your choice (1-4): "))

    print()

    # Handle user input
    # Add contacts
    if option == 1:
        # User inputs new contact information
        name = input("Enter the name of the contact: ")
        print()
        phone = input("Enter the phone number of the contact (10 digits): ")

        # Validate phone number; check for 10 digits or letters
        while len(phone) != 10 or not phone.isdigit():
            print("Invalid phone number! Please enter a 10-digit number.")
            print()
            phone = input("Enter the phone number of the contact (10 digits): ")

        # Add new contact to dictionary
        contacts[name] = phone
        print("Contact added successfully!")
    # Remove contacts
    elif option == 2:
        # User inputs contact name to remove
        name = input("Enter the name of the contact to remove: ")

        # Check if contact exists in dictionary
        if name in contacts:
            del contacts[name]
            print("Contact removed successfully!")
        else:
            print("Contact not found!")
            print("Try again")
    # List all contacts
    elif option == 3:
        # Print all contacts
        if contacts:
            print("Current contacts:")
            print()
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found!")
            print("Add some new contacts first!")
    # Exit the program
    elif option == 4:
        print("Exiting the program...")
        break
