
DB_FILE = "passwords.db"

def create_database(conn):
    """Creates the database and tables."""
    c = conn.cursor()

    # Create master_password table
    c.execute("""
        CREATE TABLE IF NOT EXISTS master_password (
            id INTEGER PRIMARY KEY,
            hashed_password BLOB NOT NULL,
            salt BLOB NOT NULL
        )
    """)

    # Create passwords table
    c.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            encrypted_password BLOB NOT NULL
        )
    """)

    conn.commit()

def store_master_password(conn, hashed_password, salt):
    """Stores the master password hash and salt in the database."""
    c = conn.cursor()
    c.execute("INSERT INTO master_password (hashed_password, salt) VALUES (?, ?)", (hashed_password, salt))
    conn.commit()

def get_master_password(conn):
    """Retrieves the master password hash and salt from the database."""
    c = conn.cursor()
    c.execute("SELECT hashed_password, salt FROM master_password LIMIT 1")
    result = c.fetchone()
    return result

def store_password(conn, service, username, encrypted_password):
    """Stores a new password in the database."""
    c = conn.cursor()
    c.execute("INSERT INTO passwords (service, username, encrypted_password) VALUES (?, ?, ?)", (service, username, encrypted_password))
    conn.commit()

def get_password(conn, service):
    """Retrieves a password from the database."""
    c = conn.cursor()
    c.execute("SELECT encrypted_password FROM passwords WHERE service = ?", (service,))
    result = c.fetchone()
    return result
