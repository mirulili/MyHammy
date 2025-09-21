### data/database.py ###
import sqlite3

DATABASE_PATH = "hamster_tracking.db"

def init_database():
    """
    Create database files and initialize table.
    """
    conn = sqlite3.connect(DATABASE_PATH)
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
    conn.close()

def save_tracking_log(log_type, data):
    """
    Save analyzed data to database.
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO activity_log (timestamp, activity_type, details) VALUES (?, ?, ?)", 
                   (timestamp, log_type, data))
    
    conn.commit()
    conn.close()
    print(f"[{timestamp}] {log_type}: {data} Data successfully saved.")