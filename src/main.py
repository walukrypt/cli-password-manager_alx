
import os
import click
import sqlite3
from src import crypto
from src import database

@click.group()
def cli():
    """A simple command-line password manager."""
    pass

@cli.command()
def init():
    """Initializes the password manager."""
    if os.path.exists(database.DB_FILE):
        click.echo("Password manager has already been initialized.")
        return

    click.echo("Initializing the password manager...")
    master_password = click.prompt("Please enter a master password", hide_input=True, confirmation_prompt=True)
    
    salt = os.urandom(16)
    hashed_password = crypto.hash_password(master_password, salt)
    
    conn = sqlite3.connect(database.DB_FILE)
    database.create_database(conn)
    database.store_master_password(conn, hashed_password, salt)
    conn.close()
    
    crypto.generate_key()
    
    click.echo("Password manager initialized.")

@cli.command()
@click.argument("service")
@click.argument("username")
@click.argument("password")
def add(service, username, password):
    """Adds a new password to the database."""
    if not os.path.exists(database.DB_FILE):
        click.echo("Password manager has not been initialized. Please run 'init' first.")
        return

    master_password = click.prompt("Please enter your master password", hide_input=True)
    
    conn = sqlite3.connect(database.DB_FILE)
    hashed_password, salt = database.get_master_password(conn)

    try:
        crypto.verify_password(master_password, salt, hashed_password)
    except Exception:
        click.echo("Invalid master password.")
        conn.close()
        return

    click.echo(f"Adding password for {service}...")
    key = crypto.load_key()
    encrypted_password = crypto.encrypt(password.encode(), key)
    database.store_password(conn, service, username, encrypted_password)
    conn.close()
    click.echo(f"Password for {service} added.")

@cli.command()
@click.argument("service")
def get(service):
    """Retrieves a password from the database."""
    if not os.path.exists(database.DB_FILE):
        click.echo("Password manager has not been initialized. Please run 'init' first.")
        return

    master_password = click.prompt("Please enter your master password", hide_input=True)
    
    conn = sqlite3.connect(database.DB_FILE)
    hashed_password, salt = database.get_master_password(conn)

    try:
        crypto.verify_password(master_password, salt, hashed_password)
    except Exception:
        click.echo("Invalid master password.")
        conn.close()
        return

    click.echo(f"Retrieving password for {service}...")
    encrypted_password = database.get_password(conn, service)
    conn.close()

    if encrypted_password is None:
        click.echo(f"No password found for {service}.")
        return

    key = crypto.load_key()
    decrypted_password = crypto.decrypt(encrypted_password[0], key)
    click.echo(f"Password for {service}: {decrypted_password.decode()}")

if __name__ == "__main__":
    cli()
