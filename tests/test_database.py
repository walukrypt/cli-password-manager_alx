
import unittest
import sqlite3
from src import database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        """Set up a temporary in-memory database before each test."""
        self.conn = sqlite3.connect(':memory:')
        database.create_database(self.conn)

    def tearDown(self):
        """Close the database connection after each test."""
        self.conn.close()

    def test_create_database(self):
        """Test that the database and tables are created."""
        c = self.conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='master_password'")
        self.assertIsNotNone(c.fetchone())
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='passwords'")
        self.assertIsNotNone(c.fetchone())

    def test_store_and_get_master_password(self):
        """Test that the master password can be stored and retrieved."""
        hashed_password = b'some_hash'
        salt = b'some_salt'
        database.store_master_password(self.conn, hashed_password, salt)
        retrieved_password, retrieved_salt = database.get_master_password(self.conn)
        self.assertEqual(hashed_password, retrieved_password)
        self.assertEqual(salt, retrieved_salt)

    def test_store_and_get_password(self):
        """Test that a password can be stored and retrieved."""
        service = "test_service"
        username = "test_user"
        encrypted_password = b'encrypted_password'
        database.store_password(self.conn, service, username, encrypted_password)
        retrieved_password = database.get_password(self.conn, service)
        self.assertEqual(encrypted_password, retrieved_password[0])

if __name__ == "__main__":
    unittest.main()
