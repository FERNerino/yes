# Define the main menu function
def main_menu():
    print("Welcome to the Groceries System!")
    print("1. Insert Item")
    print("2. Delete Item")
    print("3. Update Item")
    print("4. Stock Replenishment")
    print("5. View Replenishment")
    print("6. Stock Taking")
    print("7. Search Item")
    print("8. Add New User")
    print("9. Exit")

# Define the login function
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open("userdata.txt", "r") as file:
        for line in file:
            values = line.strip().split()
            if len(values) == 4:
                user_id, user_name, user_password, user_type = values
                if username == user_name and password == user_password:
                    print("Login successful!")
                    return user_type

    print("Incorrect password or username.")
    return None

# Define the add_new_user function
def add_new_user():
    user_id = input("Enter the user ID: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    user_type = input("Enter the user type (admin, inventory-checker, purchaser): ")

    with open("userdata.txt", "a") as file:
        file.write(f"{user_id}\t{username}\t{password}\t{user_type}\n")

    print("New user added successfully!")
    
# Main program loop
while True:
    user_type = login()
    if user_type is None:
        continue

    while True:
        main_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            if user_type == "admin":
                insert_item()
            else:
                print("Access denied.")
        elif choice == 2:
            if user_type == "admin":
                delete_item()
            else:
                print("Access denied.")
        elif choice == 3:
            if user_type == "admin":
                Add_Inventory()
            else:
                print("Access denied.")
        elif choice == 4:
            if user_type in ["admin", "purchaser"]:
                Stock_replenishment()
            else:
                print("Access denied.")
        elif choice == 5:
            if user_type in ["admin", "purchaser"]:
                View_replenishment()
            else:
                print("Access denied.")
        elif choice == 6:
            if user_type in ["admin", "inventory-checker"]:
                stock_taking()
            else:
                print("Access denied.")
        elif choice == 7:
            if user_type in ["admin", "inventory-checker", "purchaser"]:
                search_item()
            else:
                print("Access denied.")
        elif choice == 8:
            if user_type == "admin":
                add_new_user()
            else:
                print("Access denied.")
        elif choice == 9:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")