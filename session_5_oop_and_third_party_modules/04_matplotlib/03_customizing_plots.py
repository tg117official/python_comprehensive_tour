# Import the pyplot module from Matplotlib, commonly abbreviated as plt
import matplotlib.pyplot as plt

# Data for the plot
x = [1, 2, 3, 4, 5]  # X-axis data (e.g., days of the week)
y = [10, 15, 7, 10, 9]  # Y-axis data (e.g., number of tasks completed)

# Creating a line plot
plt.plot(x, y, marker='o', linestyle='-', color='g', label='Tasks Completed')  # Create a green line plot with circle markers

# Customizing the plot with labels and title
plt.xlabel('Day of the Week')  # Label for the X-axis
plt.ylabel('Number of Tasks')  # Label for the Y-axis
plt.title('Weekly Task Completion')  # Title of the plot

# Adding a legend to the plot
plt.legend(loc='upper right')  # Display legend in the upper left corner

# Finally, display the plot
plt.show()

# # Explanation of the Script
#
# 1. Importing Matplotlib:
#    - We start by importing the `pyplot` module from Matplotlib as `plt`. This module contains functions that allow for easy plotting of data.
#
# 2. Setting Up Data:
#    - The `x` list represents sequential data, such as days of the week.
#    - The `y` list contains corresponding values like the number of tasks completed each day.
#
# 3. Creating a Line Plot:
#    - `plt.plot()` is used to draw a line plot. We specify `marker='o'` for circle markers on each data point, `linestyle='-'` for a solid line, and `color='g'` for green color. The `label` is set to 'Tasks Completed' to describe the data series.
#
# 4. Customizing the Plot:
#    - `plt.xlabel()` and `plt.ylabel()` are used to add readable labels to the X-axis and Y-axis, respectively, enhancing the interpretability of the plot.
#    - `plt.title()` sets a title for the plot, "Weekly Task Completion", which provides a concise summary of what the plot displays.
#
# 5. Adding a Legend:
#    - `plt.legend()` is used to place a legend on the plot. The `loc='upper left'` argument positions the legend in the upper left corner of the plot area. The legend helps to identify what the plotted line represents, especially useful in plots with multiple data series.
#
# 6. Displaying the Plot:
#    - `plt.show()` displays the plot in a window, allowing the viewer to see the visual representation of the data.
