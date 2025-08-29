# Import the pyplot module from Matplotlib, commonly abbreviated as plt
import matplotlib.pyplot as plt

# Create data for plotting
x = [1, 2, 3, 4, 5]  # X-axis data (e.g., days of the week)
y = [2, 3, 5, 7, 11]  # Y-axis data (e.g., number of sales)

# Create a line plot: plotting y versus x
plt.plot(x, y, label='Sales Over Days')  # 'label' names the line, which will show up in the legend

# Adding labels and a title
plt.xlabel('Day')  # Label for the X-axis
plt.ylabel('Sales')  # Label for the Y-axis
plt.title('Sales Trend')  # Title of the plot

# Display a legend to explain which line represents what
plt.legend()

# Show the plot on the screen
plt.show()


# Explanation of the Script
#
# 1. Importing Matplotlib:
#    - We import the `pyplot` module from Matplotlib and nickname it `plt` for ease
#      of use.
#
# 2. Creating Data:
#    - We define two lists, `x` and `y`. `x` represents the days of the week, and
#      `y` represents something like sales numbers on those days.
#
# 3. Plotting Data:
#    - We use `plt.plot()` to create a line plot. We pass `x` and `y` as parameters,
#      along with a `label` that describes the data series.
#
# 4. Adding Labels and Title:
#    - `plt.xlabel()` and `plt.ylabel()` are used to label the X-axis and Y-axis.
#    - `plt.title()` adds a title at the top of the plot.
#
# 5. Displaying the Legend:
#    - `plt.legend()` is used to display a legend on the plot, which helps identify
#      what each line represents.
#
# 6. Displaying the Plot:
#    - Finally, `plt.show()` is called to display the plot. This opens up a window
#      with the graph, showing the trend of sales over the days.
#
#   This script provides a straightforward example of using Matplotlib for data
#   visualization, demonstrating how it can visually represent data trends, which
#   is essential for quick analysis and insights.
