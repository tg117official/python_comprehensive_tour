import matplotlib.pyplot as plt
import os

# Ensure the 'reports' folder exists
os.makedirs("reports", exist_ok=True)

def plot_sales_by_region(sales_by_region):
    """Plot sales by region as a bar chart."""
    plt.figure(figsize=(8, 5))
    sales_by_region.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Total Sales by Region", fontsize=14)
    plt.xlabel("Region", fontsize=12)
    plt.ylabel("Total Sales", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("reports/sales_by_region.png")
    plt.close()
    print("Sales by region report saved as 'reports/sales_by_region.png'")

def plot_sales_by_category(sales_by_category):
    """Plot sales by category as a pie chart."""
    plt.figure(figsize=(6, 6))
    sales_by_category.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
    plt.title("Sales Distribution by Category", fontsize=14)
    plt.ylabel("")  # Remove y-axis label for better visuals
    plt.tight_layout()
    plt.savefig("reports/sales_by_category.png")
    plt.close()
    print("Sales by category report saved as 'reports/sales_by_category.png'")

def plot_sales_trend(sales_trend):
    """Plot sales trend over time as a line chart."""
    plt.figure(figsize=(8, 5))
    sales_trend.plot(kind='line', marker='o', color='green')
    plt.title("Sales Trend Over Time", fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Total Sales", fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("reports/sales_trend.png")
    plt.close()
    print("Sales trend report saved as 'reports/sales_trend.png'")
