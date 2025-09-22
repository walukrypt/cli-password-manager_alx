
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

# This is not a secure way to store a key.
# In a real application, you would use a secure key management system.
# For this example, we will generate a key and store it in a file.
KEY_FILE = "secret.key"

def generate_key():
    """Generates a new key and saves it to a file."""
    key = AESGCM.generate_key(bit_length=128)
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_key():
    """Loads the key from the specified file."""
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt(data, key):
    """Encrypts the given data using AES-GCM."""
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, data, None)
    return nonce + ct

def decrypt(encrypted_data, key):
    """Decrypts the given data using AES-GCM."""
    aesgcm = AESGCM(key)
    nonce = encrypted_data[:12]
    ct = encrypted_data[12:]
    return aesgcm.decrypt(nonce, ct, None)

def hash_password(password, salt):
    """Hashes the given password using Scrypt."""
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def verify_password(password, salt, expected_hash):
    """Verifies the given password against the expected hash."""
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=default_backend()
    )
    kdf.verify(password.encode(), expected_hash)
