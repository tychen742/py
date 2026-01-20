<VSCode.Cell language="markdown">
## Database Best Practices and Error Handling

When working with databases in production applications, you need to follow best practices to ensure reliability, security, and maintainability.

### Connection Management
- Always close database connections
- Use context managers (`with` statements) when possible
- Handle connection errors gracefully

### SQL Security
- **Never** use string formatting to build SQL queries (SQL injection risk)
- Always use parameterized queries with placeholders (`?`)
- Validate input data before database operations

### Transaction Management
- Use transactions for operations that must complete together
- Commit changes explicitly
- Roll back on errors to maintain data consistency

### Error Handling
- Wrap database operations in try/except blocks
- Handle specific database exceptions
- Provide meaningful error messages to users
- Log errors for debugging

These practices help you build robust, secure database applications.
</VSCode.Cell>
<VSCode.Cell language="python">
# Database Best Practices and Error Handling

import sqlite3
import sys

class DatabaseManager:
    """A class demonstrating database best practices."""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def connect(self):
        """Establish database connection with error handling."""
        try:
            self.connection = sqlite3.connect(self.db_name)
            print(f"✅ Connected to {self.db_name}")
            return True
        except sqlite3.Error as e:
            print(f"❌ Database connection error: {e}")
            return False
    
    def close(self):
        """Close database connection safely."""
        if self.connection:
            self.connection.close()
            print(f"✅ Disconnected from {self.db_name}")
    
    def create_user_table(self):
        """Create users table with error handling."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    created_date TEXT DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            self.connection.commit()
            print("✅ Users table created/verified")
            return True
        except sqlite3.Error as e:
            print(f"❌ Error creating table: {e}")
            return False
    
    def add_user(self, username, email):
        """Add user with proper error handling and validation."""
        # Input validation
        if not username or not email:
            print("❌ Username and email are required")
            return False
        
        if '@' not in email:
            print("❌ Invalid email format")
            return False
        
        try:
            cursor = self.connection.cursor()
            # Use parameterized query (safe from SQL injection)
            cursor.execute('''
                INSERT INTO users (username, email) 
                VALUES (?, ?)
            ''', (username, email))
            self.connection.commit()
            print(f"✅ Added user: {username}")
            return True
            
        except sqlite3.IntegrityError as e:
            if 'username' in str(e):
                print(f"❌ Username '{username}' already exists")
            elif 'email' in str(e):
                print(f"❌ Email '{email}' already exists")
            else:
                print(f"❌ Data integrity error: {e}")
            return False
        except sqlite3.Error as e:
            print(f"❌ Database error: {e}")
            return False
    
    def get_user(self, username):
        """Get user with error handling."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT id, username, email, created_date 
                FROM users 
                WHERE username = ?
            ''', (username,))
            
            user = cursor.fetchone()
            if user:
                return {
                    'id': user[0],
                    'username': user[1], 
                    'email': user[2],
                    'created_date': user[3]
                }
            else:
                print(f"❌ User '{username}' not found")
                return None
                
        except sqlite3.Error as e:
            print(f"❌ Error retrieving user: {e}")
            return None
    
    def transaction_example(self):
        """Demonstrate transaction management."""
        cursor = self.connection.cursor()
        
        try:
            # Begin transaction (auto-starts with first SQL command)
            print("Starting transaction...")
            
            # Multiple related operations that should succeed or fail together
            cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', 
                         ('temp_user1', 'temp1@email.com'))
            cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', 
                         ('temp_user2', 'temp2@email.com'))
            
            # Simulate an error condition
            # cursor.execute('INSERT INTO users (username, email) VALUES (?, ?)', 
            #              ('temp_user1', 'duplicate@email.com'))  # Would cause error
            
            # If we get here, commit the transaction
            self.connection.commit()
            print("✅ Transaction committed successfully")
            
            # Clean up the temp users
            cursor.execute('DELETE FROM users WHERE username LIKE ?', ('temp_user%',))
            self.connection.commit()
            print("✅ Cleaned up temporary users")
            
        except sqlite3.Error as e:
            # Roll back the transaction on error
            self.connection.rollback()
            print(f"❌ Transaction rolled back due to error: {e}")

# Demonstrate best practices
print("=== DATABASE BEST PRACTICES DEMO ===")

# Using context manager for automatic cleanup
try:
    # Create and use database manager
    db = DatabaseManager('users_demo.db')
    
    if not db.connect():
        sys.exit("Failed to connect to database")
    
    # Create table
    if not db.create_user_table():
        sys.exit("Failed to create table")
    
    print("\n1. Adding users with validation:")
    
    # Valid users
    db.add_user("alice123", "alice@example.com")
    db.add_user("bob456", "bob@example.com")
    
    # Invalid inputs (will be rejected)
    db.add_user("", "charlie@example.com")      # Empty username
    db.add_user("dave", "invalid-email")        # Invalid email
    db.add_user("alice123", "alice2@example.com")  # Duplicate username
    
    print("\n2. Retrieving users:")
    alice = db.get_user("alice123")
    if alice:
        print(f"Found user: {alice['username']} ({alice['email']})")
    
    nonexistent = db.get_user("nobody")  # Will show error message
    
    print("\n3. Transaction example:")
    db.transaction_example()
    
    print("\n4. Listing all users:")
    cursor = db.connection.cursor()
    cursor.execute('SELECT username, email FROM users ORDER BY username')
    for user in cursor.fetchall():
        print(f"  {user[0]} - {user[1]}")

except Exception as e:
    print(f"❌ Unexpected error: {e}")
finally:
    # Always close the connection
    if 'db' in locals():
        db.close()

print("\n✅ Best practices demo completed!")
</VSCode.Cell>
<VSCode.Cell language="markdown">
## Real-World Application: Personal Library Database

Let's build a complete database application that manages a personal library. This example demonstrates how to design a database schema, implement all CRUD operations, and create a user-friendly interface.

### Database Design
Our library system will track:
- **Books**: Title, author, ISBN, publication year, genre
- **Authors**: Name, birth year, nationality  
- **Reading Status**: Currently reading, completed, want to read
- **Reviews**: Personal ratings and notes

This design shows how to:
- Create related tables with foreign keys
- Handle many-to-many relationships
- Implement data validation and constraints
- Build a complete application interface
</VSCode.Cell>
<VSCode.Cell language="python">
# Real-World Application: Personal Library Database

import sqlite3
import datetime
from typing import List, Dict, Optional

class LibraryManager:
    """Complete library management system demonstrating database application design."""
    
    def __init__(self, db_path='personal_library.db'):
        self.db_path = db_path
        self.connection = None
        self.setup_database()
    
    def connect(self):
        """Connect to the database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row  # Enable column access by name
            return True
        except sqlite3.Error as e:
            print(f"Database connection error: {e}")
            return False
    
    def setup_database(self):
        """Create database schema."""
        if not self.connect():
            return False
        
        try:
            cursor = self.connection.cursor()
            
            # Authors table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS authors (
                    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    birth_year INTEGER,
                    nationality TEXT,
                    created_date TEXT DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Books table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    isbn TEXT UNIQUE,
                    publication_year INTEGER,
                    genre TEXT,
                    pages INTEGER,
                    description TEXT,
                    created_date TEXT DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Book-Author relationship (many-to-many)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS book_authors (
                    book_id INTEGER,
                    author_id INTEGER,
                    PRIMARY KEY (book_id, author_id),
                    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
                    FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE
                )
            ''')
            
            # Reading status and reviews
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS reading_log (
                    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_id INTEGER,
                    status TEXT CHECK(status IN ('want_to_read', 'reading', 'completed')) DEFAULT 'want_to_read',
                    rating INTEGER CHECK(rating >= 1 AND rating <= 5),
                    review TEXT,
                    start_date TEXT,
                    finish_date TEXT,
                    created_date TEXT DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE
                )
            ''')
            
            self.connection.commit()
            print("✅ Library database schema created/verified")
            return True
            
        except sqlite3.Error as e:
            print(f"Error setting up database: {e}")
            return False
    
    def add_author(self, name: str, birth_year: Optional[int] = None, nationality: Optional[str] = None) -> Optional[int]:
        """Add an author to the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO authors (name, birth_year, nationality) 
                VALUES (?, ?, ?)
            ''', (name, birth_year, nationality))
            self.connection.commit()
            author_id = cursor.lastrowid
            print(f"✅ Added author: {name} (ID: {author_id})")
            return author_id
        except sqlite3.Error as e:
            print(f"Error adding author: {e}")
            return None
    
    def add_book(self, title: str, authors: List[str], isbn: Optional[str] = None, 
                publication_year: Optional[int] = None, genre: Optional[str] = None,
                pages: Optional[int] = None, description: Optional[str] = None) -> Optional[int]:
        """Add a book and associate it with authors."""
        try:
            cursor = self.connection.cursor()
            
            # Insert book
            cursor.execute('''
                INSERT INTO books (title, isbn, publication_year, genre, pages, description) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (title, isbn, publication_year, genre, pages, description))
            
            book_id = cursor.lastrowid
            
            # Associate with authors
            for author_name in authors:
                # Find or create author
                cursor.execute('SELECT author_id FROM authors WHERE name = ?', (author_name,))
                author = cursor.fetchone()
                
                if author:
                    author_id = author['author_id']
                else:
                    author_id = self.add_author(author_name)
                
                # Link book and author
                cursor.execute('INSERT INTO book_authors (book_id, author_id) VALUES (?, ?)', 
                             (book_id, author_id))
            
            self.connection.commit()
            print(f"✅ Added book: {title} (ID: {book_id})")
            return book_id
            
        except sqlite3.IntegrityError as e:
            print(f"Book with ISBN {isbn} already exists" if isbn else f"Integrity error: {e}")
            return None
        except sqlite3.Error as e:
            print(f"Error adding book: {e}")
            return None
    
    def update_reading_status(self, book_id: int, status: str, rating: Optional[int] = None, 
                            review: Optional[str] = None) -> bool:
        """Update reading status for a book."""
        try:
            cursor = self.connection.cursor()
            
            # Check if log entry exists
            cursor.execute('SELECT log_id FROM reading_log WHERE book_id = ?', (book_id,))
            existing = cursor.fetchone()
            
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            
            if existing:
                # Update existing entry
                update_fields = ['status = ?']
                values = [status]
                
                if rating:
                    update_fields.append('rating = ?')
                    values.append(rating)
                
                if review:
                    update_fields.append('review = ?')
                    values.append(review)
                
                if status == 'reading' and existing:
                    update_fields.append('start_date = ?')
                    values.append(current_date)
                elif status == 'completed':
                    update_fields.append('finish_date = ?')
                    values.append(current_date)
                
                values.append(book_id)
                
                cursor.execute(f'''
                    UPDATE reading_log 
                    SET {', '.join(update_fields)}
                    WHERE book_id = ?
                ''', values)
            else:
                # Create new entry
                start_date = current_date if status == 'reading' else None
                finish_date = current_date if status == 'completed' else None
                
                cursor.execute('''
                    INSERT INTO reading_log (book_id, status, rating, review, start_date, finish_date)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (book_id, status, rating, review, start_date, finish_date))
            
            self.connection.commit()
            print(f"✅ Updated reading status to: {status}")
            return True
            
        except sqlite3.Error as e:
            print(f"Error updating reading status: {e}")
            return False
    
    def search_books(self, search_term: str) -> List[Dict]:
        """Search books by title or author."""
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT DISTINCT b.book_id, b.title, b.publication_year, b.genre,
                       GROUP_CONCAT(a.name, ', ') as authors,
                       rl.status, rl.rating
                FROM books b
                LEFT JOIN book_authors ba ON b.book_id = ba.book_id
                LEFT JOIN authors a ON ba.author_id = a.author_id
                LEFT JOIN reading_log rl ON b.book_id = rl.book_id
                WHERE b.title LIKE ? OR a.name LIKE ?
                GROUP BY b.book_id
                ORDER BY b.title
            ''', (f'%{search_term}%', f'%{search_term}%'))
            
            return [dict(row) for row in cursor.fetchall()]
            
        except sqlite3.Error as e:
            print(f"Error searching books: {e}")
            return []
    
    def get_reading_stats(self) -> Dict:
        """Get reading statistics."""
        try:
            cursor = self.connection.cursor()
            
            # Total books by status
            cursor.execute('''
                SELECT status, COUNT(*) as count
                FROM reading_log
                GROUP BY status
            ''')
            status_counts = {row['status']: row['count'] for row in cursor.fetchall()}
            
            # Average rating
            cursor.execute('SELECT AVG(rating) as avg_rating FROM reading_log WHERE rating IS NOT NULL')
            avg_rating = cursor.fetchone()['avg_rating']
            
            # Favorite genres
            cursor.execute('''
                SELECT b.genre, COUNT(*) as count
                FROM books b
                JOIN reading_log rl ON b.book_id = rl.book_id
                WHERE b.genre IS NOT NULL AND rl.status = 'completed'
                GROUP BY b.genre
                ORDER BY count DESC
                LIMIT 5
            ''')
            favorite_genres = [dict(row) for row in cursor.fetchall()]
            
            return {
                'status_counts': status_counts,
                'average_rating': round(avg_rating, 2) if avg_rating else 0,
                'favorite_genres': favorite_genres
            }
            
        except sqlite3.Error as e:
            print(f"Error getting statistics: {e}")
            return {}
    
    def close(self):
        """Close database connection."""
        if self.connection:
            self.connection.close()

# Demo the complete library system
print("=== PERSONAL LIBRARY DATABASE SYSTEM ===")

library = LibraryManager()

# Add some books
print("\n1. Adding books to library:")
book1_id = library.add_book(
    title="The Python Programming Language",
    authors=["Guido van Rossum", "Python Community"],
    publication_year=1991,
    genre="Programming",
    pages=500,
    description="The definitive guide to Python programming"
)

book2_id = library.add_book(
    title="Clean Code",
    authors=["Robert C. Martin"],
    isbn="978-0132350884",
    publication_year=2008,
    genre="Programming",
    pages=464,
    description="A handbook of agile software craftsmanship"
)

book3_id = library.add_book(
    title="The Hobbit",
    authors=["J.R.R. Tolkien"],
    publication_year=1937,
    genre="Fantasy",
    pages=310,
    description="A fantasy adventure story"
)

# Update reading status
print("\n2. Updating reading status:")
if book1_id:
    library.update_reading_status(book1_id, 'completed', rating=5, 
                                review="Excellent introduction to Python!")

if book2_id:
    library.update_reading_status(book2_id, 'reading')

if book3_id:
    library.update_reading_status(book3_id, 'want_to_read')

# Search functionality
print("\n3. Searching books:")
python_books = library.search_books("Python")
print(f"Found {len(python_books)} Python-related books:")
for book in python_books:
    print(f"  • {book['title']} by {book['authors']} - Status: {book['status']}")

programming_books = library.search_books("Martin")
print(f"\\nFound {len(programming_books)} books by Martin:")
for book in programming_books:
    print(f"  • {book['title']} by {book['authors']}")

# Reading statistics
print("\n4. Reading Statistics:")
stats = library.get_reading_stats()
print(f"  Books completed: {stats['status_counts'].get('completed', 0)}")
print(f"  Currently reading: {stats['status_counts'].get('reading', 0)}")
print(f"  Want to read: {stats['status_counts'].get('want_to_read', 0)}")
print(f"  Average rating: {stats['average_rating']}/5")

if stats['favorite_genres']:
    print("  Favorite genres:")
    for genre in stats['favorite_genres']:
        print(f"    - {genre['genre']}: {genre['count']} books")

library.close()
print("\n✅ Library system demo completed!")
</VSCode.Cell>
<VSCode.Cell language="markdown">
## Chapter Summary

In this chapter, you learned how to work with databases using SQLite and Python:

### Key Concepts Mastered

1. **Database Fundamentals**
   - Understanding what databases are and why they're useful
   - Database terminology: tables, records, fields, keys, schemas
   - Advantages of databases over simple file storage

2. **SQL Basics**
   - Data Definition Language (DDL): CREATE TABLE, constraints, data types
   - Data Manipulation Language (DML): INSERT, SELECT, UPDATE, DELETE
   - CRUD operations as the foundation of database work

3. **Python Database Programming**
   - Using sqlite3 module for database operations
   - Proper connection management and error handling
   - Parameterized queries for security (preventing SQL injection)

4. **Advanced Database Skills**
   - Complex queries with JOIN operations
   - Aggregation functions: COUNT, SUM, AVG, MIN, MAX
   - Sorting, filtering, and grouping data
   - Transaction management for data integrity

5. **Best Practices Applied**
   - Input validation and error handling
   - Secure query construction with parameters
   - Proper resource management (closing connections)
   - Database design principles and relationships

6. **Real-World Application**
   - Complete library management system
   - Schema design with related tables
   - Full CRUD implementation with user interface
   - Statistics and reporting functionality

### Professional Skills Developed

- **Database Design**: Creating efficient, normalized database schemas
- **SQL Proficiency**: Writing complex queries for data analysis
- **Application Development**: Building complete database-driven applications
- **Security Awareness**: Understanding and preventing SQL injection attacks
- **Error Handling**: Robust error management for database operations

### Moving Forward

Database skills are essential for most software applications. You can now:
- Design database schemas for real-world problems
- Build applications that store and retrieve data efficiently
- Write complex SQL queries for data analysis
- Follow security best practices in database programming
- Handle errors gracefully and maintain data integrity

Practice these skills by building your own database applications. Consider exploring:
- Web applications with database backends
- Data analysis and reporting systems
- Inventory management systems
- Personal productivity applications

The foundation you've built with SQLite will transfer to other database systems like PostgreSQL, MySQL, and MongoDB as your projects grow in complexity.
</VSCode.Cell>