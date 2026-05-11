import pandas as pd

def clean_data(records):
    if not records:
        return pd.DataFrame()

    df = pd.DataFrame(records)

    df["title"] = df["title"].str.lower().str.strip()
    df["company"] = df["company"].str.strip()

    df.drop_duplicates(
        subset=["title", "company", "location"],
        inplace=True
    )

    df.fillna("Not Available", inplace=True)
    return df
