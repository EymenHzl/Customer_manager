# Initialize an empty dictionary to store customer information
customers = {}

# Initialize a variable to keep track of the next customer ID
next_customer_id = 1

# Function to list all customers
def list_customers():
    print("\nCurrent customers:\n")
    for customer_id, customer in customers.items():
        print(f"{customer_id}: {customer['name']} {customer['surname']}")

# Function to list all customers including all their information
def list_all_customers():
    print("\nCurrent customers:\n")
    for customer_id, customer in customers.items():
        print(f"{customer_id}: {customer} ")

# Function to add a new customer
def add_customer():
    global next_customer_id
    name = input("Enter customer's name: ")
    surname = input("Enter customer's surname: ")
    phone = input("Enter customer's phone number: ")

    customer = {
        "name": name,
        "surname": surname,
        "phone": phone
    }
    customers[next_customer_id] = customer
    print("Customer successfully added!")
    list_customers()
    next_customer_id += 1

# Function to delete a customer
def delete_customer():
    print("These are current customers:\n")
    list_customers()
    delete_choice = int(input("Choose a number from the list to delete: "))
    if delete_choice in customers:
        del customers[delete_choice]
        renumber_customers()
    else:
        print("Invalid customer number. No customer deleted.")

# Function to renumber customer IDs after deletion
def renumber_customers():
    global next_customer_id
    next_customer_id = 1
    new_customers = {}
    for customer_id in customers:
        new_customers[next_customer_id] = customers[customer_id]
        next_customer_id += 1
    customers.clear()
    customers.update(new_customers)

# Function to edit customer information
def edit_customer():
    print("These are current customers:\n")
    list_customers()
    edit_choice = int(input("Choose a number from the list to edit: "))
    
    if edit_choice in customers:
        customer_to_edit = customers[edit_choice]
        
        print(f"Editing customer {edit_choice}: {customer_to_edit['name']} {customer_to_edit['surname']}")
        
        name = input("Enter new name (press Enter to keep current): ")
        if name:
            customer_to_edit['name'] = name
        
        surname = input("Enter new surname (press Enter to keep current): ")
        if surname:
            customer_to_edit['surname'] = surname
        
        phone = input("Enter new phone number (press Enter to keep current): ")
        if phone:
            customer_to_edit['phone'] = phone
        
        print(f"Customer {edit_choice} has been updated:")
        print(f"{customer_to_edit['name']} {customer_to_edit['surname']} - {customer_to_edit['phone']}")
    else:
        print("Invalid customer number. No customer edited.")

# Main loop for the Customer Management System
while True:
    print("Welcome to Customer Management System (CMS)")
    print("1: Add customer")
    print("2: Delete customer")
    print("3: Edit customer")
    print("4: List all customers")
    print("5: Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_customer()
    elif choice == 2:
        delete_customer()
    elif choice == 3:
        edit_customer()
    elif choice == 4:
        list_all_customers()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please enter a valid option (1, 2, 3, 4, or 5).")
