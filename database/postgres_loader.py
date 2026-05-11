import psycopg2
from config.db_config import DB_CONFIG

def load_dataframe(df):
    if df.empty:
        print("⚠️ No data to insert")
        return

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id SERIAL PRIMARY KEY,
            title TEXT,
            company TEXT,
            location TEXT,
            posted_date TEXT,
            UNIQUE(title, company, location)
        );
    """)

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO jobs (title, company, location, posted_date)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT DO NOTHING;
        """, tuple(row))

    conn.commit()
    cur.close()
    conn.close()
