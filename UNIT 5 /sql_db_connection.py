import sqlite3

def connect_to_db(db_name='example.db'):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        print(f"Successfully connected to SQLite database '{db_name}'")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None
    finally:
        if conn:
            conn.close()
            print(f"Database connection to '{db_name}' closed.")

if __name__ == "__main__":
    # Example usage:
    # A connection is opened and immediately closed within the function for this basic example.
    # For real applications, you would keep the connection open to perform operations.
    connect_to_db()
