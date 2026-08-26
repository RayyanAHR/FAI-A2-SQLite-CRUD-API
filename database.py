import os
import sqlite3
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Fetch the URL, defaulting to a local path if not found
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./tasks.db")
# Clean the string for sqlite3 connection
DB_PATH = DATABASE_URL.replace("sqlite:///", "")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create the table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    
    # Seed 3 initial tasks only if the table is completely empty
    cursor.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.executemany("""
            INSERT INTO tasks (title, done) VALUES (?, ?)
        """, [
            ("Buy groceries", False),
            ("Complete Assignment A3", False),
            ("Review Docker documentation", True)
        ])
        conn.commit()
    conn.close()