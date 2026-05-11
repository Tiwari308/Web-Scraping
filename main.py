from data_processing.cleaner import clean_data
from database.postgres_loader import load_dataframe

def run_pipeline():
    # STEP 1: Dummy data (this proves pipeline works)
    records = [
        {
            "title": "Python Developer",
            "company": "ABC Corp",
            "location": "Mumbai",
            "posted_date": "2 days ago"
        },
        {
            "title": "Python Developer",
            "company": "ABC Corp",
            "location": "Mumbai",
            "posted_date": "2 days ago"
        }
    ]

    # STEP 2: Clean the data
    clean_df = clean_data(records)

    # STEP 3: Save to PostgreSQL
    load_dataframe(clean_df)

if __name__ == "__main__":
    run_pipeline()
    print("✅ ETL Pipeline completed successfully")

