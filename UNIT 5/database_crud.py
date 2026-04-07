import sqlite3

DATABASE_NAME = 'crud_database.db'

def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()
    print("Table 'users' ensured to exist.")

def add_user(name, email):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(f"User '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: User with email '{email}' already exists.")
    finally:
        conn.close()

def view_users():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    if users:
        print("\n--- Current Users ---")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
        print("---------------------\n")
    else:
        print("No users found.")
    return users

def update_user(user_id, new_name, new_email):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (new_name, new_email, user_id))
        if cursor.rowcount == 0:
            print(f"Error: User with ID {user_id} not found.")
        else:
            conn.commit()
            print(f"User ID {user_id} updated successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: User with email '{new_email}' already exists for another user.")
    finally:
        conn.close()

def delete_user(user_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    if cursor.rowcount == 0:
        print(f"Error: User with ID {user_id} not found.")
    else:
        conn.commit()
        print(f"User ID {user_id} deleted successfully.")
    conn.close()

def main():
    create_table() # Ensure table exists on startup

    while True:
        print("\n--- Database CRUD Operations ---")
        print("1. Add User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            if name and email:
                add_user(name, email)
            else:
                print("Name and email cannot be empty.")
        elif choice == '2':
            view_users()
        elif choice == '3':
            user_id_str = input("Enter user ID to update: ")
            if not user_id_str.isdigit():
                print("Invalid ID. Please enter a number.")
                continue
            user_id = int(user_id_str)
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            if new_name and new_email:
                update_user(user_id, new_name, new_email)
            else:
                print("Name and email cannot be empty.")
        elif choice == '4':
            user_id_str = input("Enter user ID to delete: ")
            if not user_id_str.isdigit():
                print("Invalid ID. Please enter a number.")
                continue
            user_id = int(user_id_str)
            delete_user(user_id)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
