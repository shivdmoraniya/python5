import sqlite3

DATABASE_NAME = "my_database.db"

def connect_db():
    """Establishes a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def create_table(conn):
    """Creates a simple 'users' table if it doesn't exist."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        ''')
        conn.commit()
        print("Table 'users' checked/created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def insert_user(conn, name, email):
    """Inserts a new user into the 'users' table."""
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(f"User '{name}' inserted successfully.")
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Error inserting user: {e}")
        return None

def select_users(conn):
    """Selects and prints all users from the 'users' table."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email FROM users")
        users = cursor.fetchall()
        print("\n--- All Users ---")
        if not users:
            print("No users found.")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
        return users
    except sqlite3.Error as e:
        print(f"Error selecting users: {e}")
        return []

def update_user_email(conn, user_id, new_email):
    """Updates the email of a user by their ID."""
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"User ID {user_id}'s email updated to '{new_email}'.")
        else:
            print(f"User ID {user_id} not found for update.")
    except sqlite3.Error as e:
        print(f"Error updating user: {e}")

def delete_user(conn, user_id):
    """Deletes a user by their ID."""
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"User ID {user_id} deleted successfully.")
        else:
            print(f"User ID {user_id} not found for deletion.")
    except sqlite3.Error as e:
        print(f"Error deleting user: {e}")

if __name__ == "__main__":
    conn = connect_db()
    if conn:
        create_table(conn)

        # CRUD Operations
        print("\n--- Performing CRUD Operations ---")

        # Create
        user1_id = insert_user(conn, "Alice", "alice@example.com")
        user2_id = insert_user(conn, "Bob", "bob@example.com")
        insert_user(conn, "Alice", "alice@example.com") # Attempt duplicate email

        # Read
        select_users(conn)

        # Update
        if user1_id:
            update_user_email(conn, user1_id, "alice.smith@example.com")
        select_users(conn)

        # Delete
        if user2_id:
            delete_user(conn, user2_id)
        select_users(conn)

        # Close connection
        conn.close()
        print("\nDatabase connection closed.")