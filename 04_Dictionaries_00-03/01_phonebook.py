phonebook = {}  

def display_menu():  
    print("\nPhonebook Menu:")  
    print("1. Add a new contact")  
    print("2. View all contacts")  
    print("3. Search for a contact")  
    print("4. Exit")  

def add_contact():  
    name = input("Enter the name of the contact: ")  
    phone_number = input("Enter the phone number: ")  

      
    phonebook[name] = phone_number  
    print(f"Contact {name} added successfully.")  

def view_contacts():  
    if not phonebook:  
        print("The phonebook is empty.")  
        return  

    print("\nContacts in the phonebook:")  
    for name, phone_number in phonebook.items():  
        print(f"{name}: {phone_number}")  

def search_contact():  
    name = input("Enter the name of the contact you want to search for: ")  

    
    if name in phonebook:  
        print(f"Contact found: {name} - {phonebook[name]}")  
    else:  
        print(f"Contact {name} not found.")  

def main():  
    while True:  
        display_menu()  
        choice = input("Select an option (1-4): ")  

        if choice == "1":  
            add_contact()  
        elif choice == "2":  
            view_contacts()  
        elif choice == "3":  
            search_contact()  
        elif choice == "4":  
            print("Exiting the phonebook program. Goodbye!")  
            break  
        else:  
            print("Invalid option. Please try again.")  

 
if __name__ == "__main__":  
    main()  


















    