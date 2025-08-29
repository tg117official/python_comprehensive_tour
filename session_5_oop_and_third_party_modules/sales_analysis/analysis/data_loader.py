import pandas as pd

def load_data(filepath):
    """Load sales data from a CSV file."""
    try:
        df = pd.read_csv(filepath, parse_dates=["Date"])
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at {filepath}")

def clean_data(df):
    """Clean the dataset by handling missing values and data types."""
    df.dropna(inplace=True)  # Drop rows with missing values
    df["Quantity"] = df["Quantity"].astype(int)
    df["Price"] = df["Price"].astype(float)
    return df
