import sqlite3

def connect_to_db(db_name="example.db"):
    """Establishes a connection to an SQLite database."""
    try:
        conn = sqlite3.connect(db_name)
        print(f"Successfully connected to database: {db_name}")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

if __name__ == "__main__":
    # Connect to a database (it will create it if it doesn't exist)
    db_connection = connect_to_db()
    
    if db_connection:
        # Perform database operations here (e.g., create table, insert data)
        # For this example, we just connect and then close.
        print("Database connection established. Closing now.")
        db_connection.close()
