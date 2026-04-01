import sqlite3

def main():
    db_name = 'example.db'
    conn = None
    try:
        # Connect to SQLite database (creates if not exists)
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        print(f"Connected to database: {db_name}")

        # 1. Create Table (if it doesn't exist)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            )
        ''')
        print("Table 'users' created or already exists.")

        # 2. Insert Data (Create)
        print("\n--- Inserting data ---")
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 24))
        conn.commit()
        print("Inserted two users: Alice and Bob.")

        # 3. Read Data
        print("\n--- Reading all users ---")
        cursor.execute("SELECT id, name, age FROM users")
        users = cursor.fetchall()
        for user in users:
            print(user)

        # 4. Update Data
        print("\n--- Updating data ---")
        cursor.execute("UPDATE users SET age = ? WHERE name = ?", (31, "Alice"))
        conn.commit()
        print("Updated Alice's age to 31.")

        # Read updated data to confirm
        print("\n--- Reading Alice after update ---")
        cursor.execute("SELECT id, name, age FROM users WHERE name = ?", ("Alice",))
        print(cursor.fetchone())

        # 5. Delete Data
        print("\n--- Deleting data ---")
        cursor.execute("DELETE FROM users WHERE name = ?", ("Bob",))
        conn.commit()
        print("Deleted Bob.")

        # Read all data to confirm deletion
        print("\n--- Reading all users after deletion ---")
        cursor.execute("SELECT id, name, age FROM users")
        users_after_delete = cursor.fetchall()
        if not users_after_delete:
            print("No users left in the table.")
        else:
            for user in users_after_delete:
                print(user)

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    main()