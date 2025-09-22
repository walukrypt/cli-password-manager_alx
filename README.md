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

## AI Usage

This project was developed with the assistance of an AI-powered coding assistant. The AI was used for the following tasks:

*   **Scaffolding boilerplate or logic:** The AI was used to generate the initial CLI structure using `click` and to provide examples for using the `cryptography` and `sqlite3` libraries.
*   **Writing tests:** The AI was used to generate unit tests for the cryptography and database modules.
*   **Generating commit messages:** The AI was used to generate the commit message for the initial commit.
*   **Generating documentation:** The AI was used to generate the initial `README.md` file.