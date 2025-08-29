def total_sales(df):
    """Calculate total sales (Quantity * Price) for each row."""
    df["Total Sales"] = df["Quantity"] * df["Price"]
    return df

def sales_by_region(df):
    """Summarize total sales by region."""
    return df.groupby("Region")["Total Sales"].sum()

def sales_by_category(df):
    """Summarize total sales by category."""
    return df.groupby("Category")["Total Sales"].sum()
