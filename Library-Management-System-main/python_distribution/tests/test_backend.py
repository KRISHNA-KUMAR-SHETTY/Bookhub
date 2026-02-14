
import unittest
import sqlite3
import os
import sys

# Add src to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from database import setup_database_schema, get_db_connection, DB_NAME

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Use an in-memory database for testing or a temporary file
        self.test_db = 'test_library.db'
        # Mocking or patching DB name in src/database.py would be ideal, but for now 
        # we will just test the schema setup logic on a file.
        # Actually, let's just use the real file logic but control the filename via import patching if possible,
        # or just test the functions directly.
        pass

    def test_schema_creation(self):
        """Test that tables are created correctly."""
        # We need to temporarily change the DB_NAME in database module strictly for this test?
        # A better way is if get_db_connection accepted a db_name.
        # But looking at src/database.py it hardcodes DB_NAME.
        # Let's try to verify if tables exist after setup.
        
        # Ensure we are not deleting the real DB.
        # Actually, let's skip modification of the real DB and just check if we can connect 
        # and if the tables ARE there (assuming setup has run).
        
        conn = get_db_connection()
        self.assertIsNotNone(conn, "Could not connect to database")
        cursor = conn.cursor()
        
        # Check for 'book' table
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='book'")
        self.assertIsNotNone(cursor.fetchone(), "Table 'book' does not exist")
        
        # Check for 'users' table
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        self.assertIsNotNone(cursor.fetchone(), "Table 'users' does not exist")
        
        conn.close()

    def test_user_creation(self):
        """Test user operations."""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Create a test user
        username = "testuser_unique_123"
        cursor.execute("INSERT INTO users (username, useremail, userspassword) VALUES (?, ?, ?)", 
                      (username, "test@example.com", "password123"))
        conn.commit()
        
        # Verify
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()
        self.assertIsNotNone(user)
        self.assertEqual(user[1], username)
        
        # Clean up
        cursor.execute("DELETE FROM users WHERE username=?", (username,))
        conn.commit()
        conn.close()

if __name__ == '__main__':
    # Ensure schema is set up before running tests
    setup_database_schema()
    unittest.main()
