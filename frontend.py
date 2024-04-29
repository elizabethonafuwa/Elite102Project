import tkinter as tk
from tkinter import messagebox
import random
import mysql.connector

# Function to establish a connection with MySQL database
def connect_to_database():
    try:
        # Establish connection to MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="hhhggg123",
            database="elite102"
        )
        return connection
    except mysql.connector.Error as error:
        messagebox.showerror("Database Error", f"Failed to connect to database: {error}")
        return None

# Function to close the database connection
def close_database_connection(connection):
    if connection:
        connection.close()

# Function to generate a random account number
def generate_account_number():
    return random.randint(100000, 999999)

# Function to generate a random PIN
def generate_pin():
    return random.randint(1000, 9999)

# Function to create a new user account
def create_account(first_name, last_name):
    account_number = generate_account_number()
    pin = generate_pin()
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO user_accounts (account_number, pin, first_name, last_name, balance) VALUES (%s, %s, %s, %s, 0)"
        cursor.execute(query, (account_number, pin, first_name, last_name))
        connection.commit()
        close_database_connection(connection)
        messagebox.showinfo("Account Created", f"Account created successfully.\nAccount Number: {account_number}\nPIN: {pin}")

# Function to check account balance
def check_balance(account_number, pin):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "SELECT balance FROM user_accounts WHERE account_number = %s AND pin = %s"
        cursor.execute(query, (account_number, pin))
        balance = cursor.fetchone()
        close_database_connection(connection)
        if balance:
            return balance[0]
        else:
            return None

# Function to deposit funds
def deposit(account_number, pin, amount):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE user_accounts SET balance = balance + %s WHERE account_number = %s AND pin = %s"
        cursor.execute(query, (amount, account_number, pin))
        connection.commit()
        close_database_connection(connection)
        messagebox.showinfo("Deposit", f"${amount} deposited successfully")

# Function to withdraw funds
def withdraw(account_number, pin, amount):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE user_accounts SET balance = balance - %s WHERE account_number = %s AND pin = %s AND balance >= %s"
        cursor.execute(query, (amount, account_number, pin, amount))
        if cursor.rowcount > 0:
            connection.commit()
            close_database_connection(connection)
            messagebox.showinfo("Withdrawal", f"${amount} withdrawn successfully")
        else:
            close_database_connection(connection)
            messagebox.showerror("Error", "Insufficient funds or invalid account number/PIN")

# Function to delete an account
def delete_account(account_number, pin):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "DELETE FROM user_accounts WHERE account_number = %s AND pin = %s"
        cursor.execute(query, (account_number, pin))
        connection.commit()
        close_database_connection(connection)
        messagebox.showinfo("Account Deleted", "Account deleted successfully")

# Function to update account details
def update_account(account_number, pin, first_name, last_name):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE user_accounts SET first_name = %s, last_name = %s WHERE account_number = %s AND pin = %s"
        cursor.execute(query, (first_name, last_name, account_number, pin))
        connection.commit()
        close_database_connection(connection)
        messagebox.showinfo("Account Updated", "Account details updated successfully")

# Function to display the welcome message
def show_welcome_screen():
    welcome_window = tk.Toplevel(root)
    welcome_window.title("Welcome")
    welcome_label = tk.Label(welcome_window, text="Welcome to Online Banking System!")
    welcome_label.pack(padx=20, pady=20)
    close_button = tk.Button(welcome_window, text="Close", command=welcome_window.destroy)
    close_button.pack(pady=10)

# Function to display the main menu
def show_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Menu")
    menu_label = tk.Label(menu_window, text="Select an option:")
    menu_label.pack(padx=20, pady=20)
    
    check_balance_button = tk.Button(menu_window, text="Check Balance", command=check_balance_menu)
    check_balance_button.pack(pady=5)
    
    deposit_button = tk.Button(menu_window, text="Deposit", command=deposit_menu)
    deposit_button.pack(pady=5)
    
    withdraw_button = tk.Button(menu_window, text="Withdraw", command=withdraw_menu)
    withdraw_button.pack(pady=5)
    
    create_account_button = tk.Button(menu_window, text="Create Account", command=create_account_menu)
    create_account_button.pack(pady=5)
    
    delete_account_button = tk.Button(menu_window, text="Delete Account", command=delete_account_menu)
    delete_account_button.pack(pady=5)
    
    update_account_button = tk.Button(menu_window, text="Update Account", command=update_account_menu)
    update_account_button.pack(pady=5)
    
    close_button = tk.Button(menu_window, text="Close", command=menu_window.destroy)
    close_button.pack(pady=10)

# Function to display the check balance menu
def check_balance_menu():
    check_balance_window = tk.Toplevel(root)
    check_balance_window.title("Check Balance")
    account_number_label = tk.Label(check_balance_window, text="Enter Account Number:")
    account_number_label.pack(pady=5)
    account_number_entry = tk.Entry(check_balance_window)
    account_number_entry.pack(pady=5)
    pin_label = tk.Label(check_balance_window, text="Enter PIN:")
    pin_label.pack(pady=5)
    pin_entry = tk.Entry(check_balance_window)
    pin_entry.pack(pady=5)
    check_button = tk.Button(check_balance_window, text="Check", command=lambda: check_balance_menu_command(int(account_number_entry.get()), int(pin_entry.get())))
    check_button.pack(pady=5)

# Function to check account balance for the provided account number and PIN
def check_balance_menu_command(account_number, pin):
    balance = check_balance(account_number, pin)
    if balance is not None:
        messagebox.showinfo("Balance", f"Your balance is ${balance}")
    else:
        messagebox.showerror("Error", "Invalid account number or PIN")

# Function to display the deposit menu
def deposit_menu():
    deposit_window = tk.Toplevel(root)
    deposit_window.title("Deposit")
    account_number_label = tk.Label(deposit_window, text="Enter Account Number:")
    account_number_label.pack(pady=5)
    account_number_entry = tk.Entry(deposit_window)
    account_number_entry.pack(pady=5)
    pin_label = tk.Label(deposit_window, text="Enter PIN:")
    pin_label.pack(pady=5)
    pin_entry = tk.Entry(deposit_window)
    pin_entry.pack(pady=5)
    amount_label = tk.Label(deposit_window, text="Enter Amount:")
    amount_label.pack(pady=5)
    amount_entry = tk.Entry(deposit_window)
    amount_entry.pack(pady=5)
    deposit_button = tk.Button(deposit_window, text="Deposit", command=lambda: deposit(int(account_number_entry.get()), int(pin_entry.get()), float(amount_entry.get())))
    deposit_button.pack(pady=5)

# Function to display the withdraw menu
def withdraw_menu():
    withdraw_window = tk.Toplevel(root)
    withdraw_window.title("Withdraw")
    account_number_label = tk.Label(withdraw_window, text="Enter Account Number:")
    account_number_label.pack(pady=5)
    account_number_entry = tk.Entry(withdraw_window)
    account_number_entry.pack(pady=5)
    pin_label = tk.Label(withdraw_window, text="Enter PIN:")
    pin_label.pack(pady=5)
    pin_entry = tk.Entry(withdraw_window)
    pin_entry.pack(pady=5)
    amount_label = tk.Label(withdraw_window, text="Enter Amount:")
    amount_label.pack(pady=5)
    amount_entry = tk.Entry(withdraw_window)
    amount_entry.pack(pady=5)
    withdraw_button = tk.Button(withdraw_window, text="Withdraw", command=lambda: withdraw(int(account_number_entry.get()), int(pin_entry.get()), float(amount_entry.get())))
    withdraw_button.pack(pady=5)

# Function to display the create account menu
def create_account_menu():
    create_account_window = tk.Toplevel(root)
    create_account_window.title("Create Account")
    first_name_label = tk.Label(create_account_window, text="First Name:")
    first_name_label.pack(pady=5)
    first_name_entry = tk.Entry(create_account_window)
    first_name_entry.pack(pady=5)
    last_name_label = tk.Label(create_account_window, text="Last Name:")
    last_name_label.pack(pady=5)
    last_name_entry = tk.Entry(create_account_window)
    last_name_entry.pack(pady=5)
    create_button = tk.Button(create_account_window, text="Create Account", command=lambda: create_account(first_name_entry.get(), last_name_entry.get()))
    create_button.pack(pady=5)

# Function to display the delete account menu
def delete_account_menu():
    delete_account_window = tk.Toplevel(root)
    delete_account_window.title("Delete Account")
    account_number_label = tk.Label(delete_account_window, text="Enter Account Number:")
    account_number_label.pack(pady=5)
    account_number_entry = tk.Entry(delete_account_window)
    account_number_entry.pack(pady=5)
    pin_label = tk.Label(delete_account_window, text="Enter PIN:")
    pin_label.pack(pady=5)
    pin_entry = tk.Entry(delete_account_window)
    pin_entry.pack(pady=5)
    delete_button = tk.Button(delete_account_window, text="Delete Account", command=lambda: delete_account(int(account_number_entry.get()), int(pin_entry.get())))
    delete_button.pack(pady=5)

# Function to display the update account menu
def update_account_menu():
    update_account_window = tk.Toplevel(root)
    update_account_window.title("Update Account")
    account_number_label = tk.Label(update_account_window, text="Enter Account Number:")
    account_number_label.pack(pady=5)
    account_number_entry = tk.Entry(update_account_window)
    account_number_entry.pack(pady=5)
    pin_label = tk.Label(update_account_window, text="Enter PIN:")
    pin_label.pack(pady=5)
    pin_entry = tk.Entry(update_account_window)
    pin_entry.pack(pady=5)
    first_name_label = tk.Label(update_account_window, text="First Name:")
    first_name_label.pack(pady=5)
    first_name_entry = tk.Entry(update_account_window)
    first_name_entry.pack(pady=5)
    last_name_label = tk.Label(update_account_window, text="Last Name:")
    last_name_label.pack(pady=5)
    last_name_entry = tk.Entry(update_account_window)
    last_name_entry.pack(pady=5)
    update_button = tk.Button(update_account_window, text="Update Account", command=lambda: update_account(int(account_number_entry.get()), int(pin_entry.get()), first_name_entry.get(), last_name_entry.get()))
    update_button.pack(pady=5)

# Create the main window
root = tk.Tk()
root.title("Online Banking System")

# Create a welcome button
welcome_button = tk.Button(root, text="Welcome", command=show_welcome_screen)
welcome_button.pack(pady=20)

# Create a menu button
menu_button = tk.Button(root, text="Menu", command=show_menu)
menu_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
