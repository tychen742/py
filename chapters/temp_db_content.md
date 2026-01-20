# Database Chapter Content to Add

```python
# First SQLite Example - Getting Started

import sqlite3
import os

# Remove existing database file if it exists (for clean start)
if os.path.exists('example.db'):
    os.remove('example.db')

print("=== Creating Your First Database ===")

# Connect to SQLite database (creates file if it doesn't exist)
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

print("✅ Connected to database 'example.db'")

# Create a simple table
cursor.execute('''
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
''')

print("✅ Created 'students' table")

# Insert some sample data
students_data = [
    ('Alice Johnson', 20, 'alice@email.com'),
    ('Bob Smith', 22, 'bob@email.com'),
    ('Carol Davis', 19, 'carol@email.com'),
    ('David Wilson', 21, 'david@email.com')
]

cursor.executemany('''
    INSERT INTO students (name, age, email) 
    VALUES (?, ?, ?)
''', students_data)

print(f"✅ Inserted {cursor.rowcount} students")

# Commit changes and close connection
connection.commit()
connection.close()

print("✅ Database saved and connection closed")
print("\nNext: Let's learn to query this data!")
```