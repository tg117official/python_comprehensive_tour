# Import the pyplot module from Matplotlib, commonly abbreviated as plt
import matplotlib.pyplot as plt

# Data for the plots
data = [25, 20, 15, 10, 30]  # Example data for histogram and bar chart
categories = ['Apples', 'Bananas', 'Oranges', 'Berries', 'Melons']  # Categories for bar and pie charts

# Creating a histogram
plt.figure(figsize=(12, 8))  # Set the size of the overall figure

plt.subplot(2, 2, 1)  # Prepare a subplot area in a 2x2 configuration, first plot
plt.hist(data, bins=2, color='blue', alpha=0.7)  # Create a histogram
plt.title('Histogram')  # Title for the histogram
plt.xlabel('Value Range')  # X-axis label for the histogram
plt.ylabel('Frequency')  # Y-axis label for the histogram

# Creating a bar chart
plt.subplot(2, 2, 2)  # Second plot in the 2x2 layout
plt.bar(categories, data, color='green', alpha=0.7)  # Create a bar chart
plt.title('Bar Chart')  # Title for the bar chart
plt.xlabel('Fruit')  # X-axis label for the bar chart
plt.ylabel('Quantity')  # Y-axis label for the bar chart

# Creating a pie chart
plt.subplot(2, 2, 3)  # Third plot in the 2x2 layout
plt.pie(data, labels=categories, autopct='%1.1f%%', startangle=90)  # Create a pie chart
plt.axis('equal')  # Ensure the pie chart is drawn as a circle
plt.title('Pie Chart')  # Title for the pie chart

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the figure
plt.show()

# 1. Importing Matplotlib:
#    - The `pyplot` module from Matplotlib is imported as `plt`, which provides plotting functions.
#
# 2. Setting Up Data:
#    - `data` and `categories` provide numerical values and corresponding categories for the plots.
#
# 3. Creating a Histogram:
#    - `plt.hist()` is used for creating histograms, with parameters like `bins` to define the number of bins, `color` for the bin color, and `alpha` for transparency.
#    - Titles and labels are added to describe the histogram's axes and content.
#
# 4. Creating a Bar Chart:
#    - `plt.bar()` plots a bar chart, using `categories` for the X-axis and `data` for the bar heights.
#    - Additional plot customization like colors and labels provide clarity and visual appeal.
#
# 5. Creating a Pie Chart:
#    - `plt.pie()` generates a pie chart, where `data` determines the sections' sizes and `labels` adds category names.
#    - `autopct` adds percentage labels to each pie section, and `startangle` rotates the start of the pie chart for better orientation.
#    - `plt.axis('equal')` ensures the pie chart is perfectly circular.
#
# 6. Adjusting Layout and Displaying the Figure:
#    - `plt.tight_layout()` adjusts subplot parameters to minimize any overlap.
#    - `plt.show()` displays the final figure with all subplots.