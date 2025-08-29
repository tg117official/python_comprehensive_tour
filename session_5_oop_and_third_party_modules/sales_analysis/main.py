from analysis.data_loader import load_data, clean_data
from analysis.data_summary import total_sales, sales_by_region, sales_by_category
from analysis.data_insights import top_selling_products, region_with_highest_sales, sales_trend
from analysis.data_visualizer import plot_sales_by_region, plot_sales_by_category, plot_sales_trend

def main():
    # Load and clean data
    filepath = "data/sales_data.csv"
    print("Loading data...")
    df = load_data(filepath)
    df = clean_data(df)

    # Add total sales column
    df = total_sales(df)

    # Generate summaries
    print("\n--- Sales Summary by Region ---")
    region_sales = sales_by_region(df)
    print(region_sales)

    print("\n--- Sales Summary by Category ---")
    category_sales = sales_by_category(df)
    print(category_sales)

    # Generate insights
    print("\n--- Top Selling Products ---")
    print(top_selling_products(df))

    region, sales = region_with_highest_sales(df)
    print(f"\n--- Region with Highest Sales ---\nRegion: {region}, Sales: ${sales:.2f}")

    trend = sales_trend(df)
    print("\n--- Sales Trend Over Time ---")
    print(trend)

    # Create visualizations and save reports
    print("\nGenerating visual reports...")
    plot_sales_by_region(region_sales)
    plot_sales_by_category(category_sales)
    plot_sales_trend(trend)

if __name__ == "__main__":
    main()
