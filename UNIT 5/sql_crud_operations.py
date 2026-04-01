import sqlite3

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """ Create a users table if it doesn't exist """
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        ''')
        conn.commit()
        print("Table 'users' created or already exists.")
    except sqlite3.Error as e:
        print(e)

def insert_user(conn, user):
    """ Insert a new user into the users table """
    sql = ''' INSERT INTO users(name,email) VALUES(?,?) '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, user)
        conn.commit()
        print(f"User '{user[0]}' inserted with ID: {cursor.lastrowid}")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Error: User with email '{user[1]}' already exists.")
        return None
    except sqlite3.Error as e:
        print(e)
        return None

def select_all_users(conn):
    """ Select all rows in the users table """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("\n--- Current Users ---")
    if not rows:
        print("No users found.")
    for row in rows:
        print(row)
    return rows

def update_user_email(conn, user_id, new_email):
    """ Update email of a user specified by user_id """
    sql = ''' UPDATE users SET email = ? WHERE id = ? '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, (new_email, user_id))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"User with ID {user_id} updated. New email: '{new_email}'")
        else:
            print(f"No user found with ID {user_id} to update.")
    except sqlite3.Error as e:
        print(e)

def delete_user(conn, user_id):
    """ Delete a user by user_id """
    sql = ''' DELETE FROM users WHERE id = ? '''
    cursor = conn.cursor()
    try:
        cursor.execute(sql, (user_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"User with ID {user_id} deleted.")
        else:
            print(f"No user found with ID {user_id} to delete.")
    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    database_file = "py_crud_example.db" # This will create a file in the same directory

    # 1. Create a database connection
    conn = create_connection(database_file)

    if conn:
        with conn: # Use 'with' statement for proper connection handling
            # 2. Create table
            create_table(conn)

            # 3. Perform Create (Insert) operations
            print("\n--- Inserting users ---")
            user1_id = insert_user(conn, ("Alice", "alice@example.com"))
            user2_id = insert_user(conn, ("Bob", "bob@example.com"))
            user3_id = insert_user(conn, ("Charlie", "charlie@example.com"))
            insert_user(conn, ("Alice Smith", "alice@example.com")) # Attempt to insert duplicate email

            # 4. Perform Read (Select) operation
            select_all_users(conn)

            # 5. Perform Update operation
            print("\n--- Updating user ---")
            if user1_id:
                update_user_email(conn, user1_id, "alice.smith@example.com")
            else:
                print("Cannot update, user1 was not inserted successfully.")
            select_all_users(conn)

            # 6. Perform Delete operation
            print("\n--- Deleting user ---")
            if user2_id:
                delete_user(conn, user2_id)
            else:
                print("Cannot delete, user2 was not inserted successfully.")
            select_all_users(conn)

            # Try deleting a non-existent user
            delete_user(conn, 999)

    else:
        print("Could not establish database connection.")
