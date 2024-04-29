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
        print(f"Failed to connect to database: {error}")
        return None

# Function to close the database connection
def close_database_connection(connection):
    if connection:
        connection.close()

# Function to check account balance
def check_balance(account_number):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "SELECT balance FROM user_accounts WHERE account_number = %s"
        cursor.execute(query, (account_number,))
        balance = cursor.fetchone()
        close_database_connection(connection)
        if balance:
            return balance[0]
        else:
            return None

# Function to deposit funds
def deposit(account_number, amount):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE user_accounts SET balance = balance + %s WHERE account_number = %s"
        cursor.execute(query, (amount, account_number))
        connection.commit()
        close_database_connection(connection)

# Function to withdraw funds
def withdraw(account_number, amount):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE user_accounts SET balance = balance - %s WHERE account_number = %s AND balance >= %s"
        cursor.execute(query, (amount, account_number, amount))
        if cursor.rowcount > 0:
            connection.commit()
            close_database_connection(connection)
            return True
        else:
            close_database_connection(connection)
            return False

# Function to create a new account
def create_account(account_number, pin, first_name, last_name):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "INSERT INTO user_accounts (account_number, pin, first_name, last_name, balance) VALUES (%s, %s, %s, %s, 0)"
        cursor.execute(query, (account_number, pin, first_name, last_name))
        connection.commit()
        close_database_connection(connection)

# Function to delete an account
def delete_account(account_number):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "DELETE FROM user_accounts WHERE account_number = %s"
        cursor.execute(query, (account_number,))
        connection.commit()
        close_database_connection(connection)

# Function to update account details
def update_account(account_number, pin, first_name, last_name):
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        query = "UPDATE user_accounts SET pin = %s, first_name = %s, last_name = %s WHERE account_number = %s"
        cursor.execute(query, (pin, first_name, last_name, account_number))
        connection.commit()
        close_database_connection(connection)
