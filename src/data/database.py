### data/database.py ###
import sqlite3
import datetime 

DATABASE_PATH = "hamster_tracking.db"

def init_database():
    """
    Create database files and initialize table.
    """
    try:
        with sqlite3.connect(DATABASE_PATH) as conn: 
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS activity_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    activity_type TEXT NOT NULL,
                    details TEXT
                )
            """)
            conn.commit()
        print("Database initialized successfully.") # Success message
    except sqlite3.Error as e: # Error handling
        print(f"Error initializing database: {e}")

def save_tracking_log(log_type: str, data: str): 
    """
    Save analyzed data to database.
    """
    try:
        with sqlite3.connect(DATABASE_PATH) as conn:
            cursor = conn.cursor()
            
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute(
                "INSERT INTO activity_log (timestamp, activity_type, details) VALUES (?, ?, ?)", 
                (timestamp, log_type, data)
            )
            
            conn.commit()
            print(f"[{timestamp}] {log_type}: {data} Data successfully saved.")
    except sqlite3.Error as e: # Error handling
        print(f"Error saving tracking log: {e}")