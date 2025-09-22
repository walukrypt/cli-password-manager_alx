
import unittest
import os
from src import crypto

class TestCrypto(unittest.TestCase):

    def setUp(self):
        """Set up for the tests."""
        self.key = crypto.generate_key()
        self.password = "mysecretpassword"
        self.salt = os.urandom(16)

    def test_key_generation(self):
        """Test that a key is generated and saved."""
        self.assertTrue(os.path.exists(crypto.KEY_FILE))
        self.assertEqual(self.key, crypto.load_key())

    def test_encryption_decryption(self):
        """Test that data can be encrypted and decrypted."""
        data = b"test data"
        encrypted_data = crypto.encrypt(data, self.key)
        decrypted_data = crypto.decrypt(encrypted_data, self.key)
        self.assertEqual(data, decrypted_data)

    def test_password_hashing_and_verification(self):
        """Test that a password can be hashed and verified."""
        hashed_password = crypto.hash_password(self.password, self.salt)
        self.assertIsNotNone(hashed_password)
        crypto.verify_password(self.password, self.salt, hashed_password)

    def test_wrong_password_verification(self):
        """Test that verification fails for a wrong password."""
        hashed_password = crypto.hash_password(self.password, self.salt)
        with self.assertRaises(Exception):
            crypto.verify_password("wrongpassword", self.salt, hashed_password)

    def tearDown(self):
        """Clean up after the tests."""
        if os.path.exists(crypto.KEY_FILE):
            os.remove(crypto.KEY_FILE)

if __name__ == "__main__":
    unittest.main()
