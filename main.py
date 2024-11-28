import os

# File paths
MENU_FILE = "menu.txt"
SALES_FILE = "sales.txt"
CREDENTIALS_FILE = "credentials.txt"

# Initialize files if they do not exist
def initialize_files():
    if not os.path.exists(MENU_FILE):
        with open(MENU_FILE, "w") as f:
            f.write("Pizza,8.99\nBurger,5.49\nPasta,7.99\n")  # Sample menu items

    if not os.path.exists(SALES_FILE):
        with open(SALES_FILE, "w") as f:
            f.write("")  # Empty sales record

    if not os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "w") as f:
            f.write("admin,admin123,admin\n")  # Admin credentials
            f.write("user,user123,user\n")    # User credentials

# Admin Panel Functions
def admin_panel():
    while True:
        print("\n--- Admin Panel ---")
        print("\n1. View Menu")
        print("2. Add Menu Item")
        print("3. Delete Menu Item")
        print("4. View Sales")
        print("5. Logout")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_menu()
        elif choice == "2":
            add_menu_item()
        elif choice == "3":
            delete_menu_item()
        elif choice == "4":
            view_sales()
        elif choice == "5":
            print("\nLogging out from Admin Panel.")
            break
        else:
            print("\nInvalid choice. Please try again.")

def view_menu():
    print("\n--- Menu ---")
    if os.path.getsize(MENU_FILE) == 0:
        print("\nThe menu is empty.")
    else:
        with open(MENU_FILE, "r") as f:
            for line in f:
                item, price = line.strip().split(",")
                print(f"\n{item} - ${price}")

def add_menu_item():
    item_name = input("\nEnter item name: ").strip()
    price = input("Enter price: ").strip()
    with open(MENU_FILE, "a") as f:
        f.write(f"\n{item_name},{price}")
    print(f"\n{item_name} added to the menu.")

def delete_menu_item():
    view_menu()
    item_name = input("\nEnter the name of the item to delete: ").strip()
    with open(MENU_FILE, "r") as f:
        lines = f.readlines()
    with open(MENU_FILE, "w") as f:
        deleted = False
        for line in lines:
            if not line.startswith(item_name + ","):
                f.write(line)
            else:
                deleted = True
        if deleted:
            print(f"\n{item_name} deleted from the menu.")
        else:
            print(f"\n{item_name} not found in the menu.")

def view_sales():
    print("\n--- Sales Records ---")
    if os.path.getsize(SALES_FILE) == 0:
        print("\nNo sales records found.")
    else:
        with open(SALES_FILE, "r") as f:
            for line in f:
                item, quantity, total = line.strip().split(",")
                print(f"{item}-Quantity: {quantity}, Total: ${total}")

# User Panel Functions
def user_panel():
    while True:
        print("\n--- User Panel ---")
        print("\n1. View Menu")
        print("2. Place Order")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_menu()
        elif choice == "2":
            place_order()
        elif choice == "3":
            print("\nLogging out from User Panel.")
            break
        else:
            print("\nInvalid choice. Please try again.")

def place_order():
    view_menu()
    item_name = input("Enter the name of the item to order: ").strip()
    quantity = int(input("Enter quantity: "))
    with open(MENU_FILE, "r") as f:
        menu = {line.split(",")[0]: float(line.split(",")[1]) for line in f}
    if item_name in menu:
        total = menu[item_name] * quantity
        print(f"\nYour total is: ${total:.2f}")
        with open(SALES_FILE, "a") as f:
            f.write(f"{item_name},{quantity},{total:.2f}\n")
        print("\nOrder placed successfully!")
    else:
        print("\nItem not found in the menu.")

# Login Function
def login():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    with open(CREDENTIALS_FILE, "r") as f:
        credentials = {line.split(",")[0]: (line.split(",")[1], line.split(",")[2].strip()) for line in f}
    if username in credentials and credentials[username][0] == password:
        print(f"\n**************  Welcome, {username}!  ********************")
        if credentials[username][1] == "admin":
            admin_panel()
        else:
            user_panel()
    else:
        print("\nInvalid credentials. Please try again.")

# Main Function
def main():
    initialize_files()
    while True:
        print("***********************************************************************")
        print("\n---------------------------- STAR RESTO -------------------------\n")
        print("***********************************************************************")
        print("\n1. Login")
        print("2. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            print("\n*****************************************************\n")
            print("\n--------------Exiting... Goodbye!-----------\n")
            print("\n*****************************************************\n")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()

