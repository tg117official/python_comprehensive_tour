def top_selling_products(df, top_n=3):
    """Identify the top N products by total sales."""
    product_sales = df.groupby("Product")["Total Sales"].sum()
    return product_sales.sort_values(ascending=False).head(top_n)

def region_with_highest_sales(df):
    """Identify the region with the highest total sales."""
    sales_by_region = df.groupby("Region")["Total Sales"].sum()
    return sales_by_region.idxmax(), sales_by_region.max()

def sales_trend(df):
    """Analyze sales trends over time."""
    return df.groupby("Date")["Total Sales"].sum()
