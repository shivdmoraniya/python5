import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# Create a table named 'students' with 3 columns if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# Insert a sample student record
student_name = "Alice"
student_age = 20
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (student_name, student_age))

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"Database 'student.db' created, table 'students' created, and a record for {student_name} inserted.")