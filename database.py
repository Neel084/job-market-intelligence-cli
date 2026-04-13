import sqlite3

DB_name = "Jobs.db"

def create_table():
    conn = sqlite3.connect(DB_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
                id TEXT PRIMARY KEY,
                title TEXT,
                company TEXT,
                location TEXT,
                salary_min REAL,
                salary_max REAL,
                description TEXT,
                created TEXT,
                url TEXT
    )
""")
    
    conn.commit()
    conn.close()

def save_jobs(jobs):
    conn = sqlite3.connect(DB_name)
    cursor = conn.cursor()

    for job in jobs:
        cursor.execute("""
            INSERT OR IGNORE INTO jobs
            (id, title, company, location, salary_min, salary_max, description, created, url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (

            job["id"],
            job["title"],
            job["company"] ["display_name"],
            job["location"] ["display_name"],
            job.get("salary_min"),
            job.get("salary_max"),
            job["description"],
            job["created"],
            job["redirect_url"]
))

    conn.commit()
    conn.close()

def get_all_jobs():
    conn = sqlite3.connect(DB_name)
    Cursor = conn.cursor()

    Cursor.execute("SELECT * FROM jobs")
    rows = Cursor.fetchall()

    conn.close()
    return rows
