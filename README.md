[![Pylint](https://github.com/yourusername/your-repo/actions/workflows/pylint.yml/badge.svg)](https://github.com/yourusername/your-repo/actions/workflows/pylint.yml)
![Pylint score](pylint.svg)

# CLI Password Manager

A simple command-line password manager built with Python.

## Features

*   **Secure Encryption:** Uses AES-GCM for strong encryption.
*   **Cross-Platform:** Works on macOS, Linux, and Windows.
*   **Simple CLI Interface:** Easy-to-use commands for managing your passwords.
*   **Master Password Protection:** Uses Scrypt for hashing and verification of a master password.

## Technologies Used

*   [Python](https://www.python.org/)
*   [click](https://click.palletsprojects.com/)
*   [cryptography](https://cryptography.io/)
*   [sqlite3](https://docs.python.org/3/library/sqlite3.html)

## Setup and Run Instructions

1.  **Prerequisites:**
    *   [Python 3](https://www.python.org/downloads/)

2.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialize the password store:**
    ```bash
    python3 -m src.main init
    ```

## Usage

### Add a new password
```bash
python3 -m src.main add <service> <username> <password>
```

### Show a password
```bash
python3 -m src.main get <service>
```
