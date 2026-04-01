import sqlite3

def connect_db(db_name='my_database.db'):
    """Connects to a SQLite database and returns the connection and cursor."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    return conn, cursor

def create_table(cursor):
    """Creates a 'users' table if it doesn't exist."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    print("Table 'users' ensured.")

def insert_user(conn, cursor, name, email):
    """Inserts a new user into the 'users' table."""
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(f"User '{name}' inserted successfully.")
    except sqlite3.IntegrityError:
        print(f"Error: User with email '{email}' already exists.")

def select_users(cursor):
    """Fetches and prints all users from the 'users' table."""
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("\n--- All Users ---")
    if users:
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    else:
        print("No users found.")
    return users

def update_user_email(conn, cursor, user_id, new_email):
    """Updates the email of a user."""
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"User with ID {user_id} updated successfully to new email: {new_email}.")
    else:
        print(f"No user found with ID {user_id}.")

def delete_user(conn, cursor, user_id):
    """Deletes a user from the 'users' table."""
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"User with ID {user_id} deleted successfully.")
    else:
        print(f"No user found with ID {user_id}.")

if __name__ == "__main__":
    conn, cursor = connect_db()
    create_table(cursor)

    # C - Create
    insert_user(conn, cursor, "Alice Smith", "alice@example.com")
    insert_user(conn, cursor, "Bob Johnson", "bob@example.com")
    insert_user(conn, cursor, "Charlie Brown", "charlie@example.com")
    insert_user(conn, cursor, "Alice Smith", "alice@example.com") # This should show an error (duplicate email)

    # R - Read
    print("\n--- Initial Users ---")
    initial_users = select_users(cursor)

    # U - Update
    # Find Alice's ID to update her email
    alice_id = None
    for user in initial_users:
        if user[1] == "Alice Smith":
            alice_id = user[0]
            break
    if alice_id:
        update_user_email(conn, cursor, alice_id, "alice.smith.new@example.com")
        print("\n--- Users After Update ---")
        select_users(cursor) # Show updated list

    # D - Delete
    # Find Bob's ID to delete him
    bob_id = None
    # Re-read users to ensure latest state for deletion
    current_users_for_delete = select_users(cursor)
    for user in current_users_for_delete:
        if user[1] == "Bob Johnson":
            bob_id = user[0]
            break
    if bob_id:
        delete_user(conn, cursor, bob_id)
        print("\n--- Users After Delete ---")
        select_users(cursor) # Show remaining list

    conn.close()
    print("\nDatabase connection closed.")