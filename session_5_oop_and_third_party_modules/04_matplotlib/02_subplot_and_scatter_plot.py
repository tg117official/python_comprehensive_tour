# Import the pyplot module from Matplotlib, commonly abbreviated as plt
import matplotlib.pyplot as plt

# Data for the plots
x = [1, 2, 3, 4, 5]  # Example data for X-axis (e.g., time in hours)
y_line = [2, 3, 2, 5, 7]  # Y-axis data for line plot (e.g., temperature in degrees)
y_scatter = [1, 4, 9, 16, 25]  # Y-axis data for scatter plot (e.g., speed in km/h)

# Creating a line plot
plt.figure(figsize=(10, 5))  # Set the size of the plot
plt.subplot(1, 2, 1)  # Prepare a subplot area, specifying 1 row, 2 columns, first plot
plt.plot(x, y_line, marker='o', color='b', label='Temperature')  # Plotting the line graph
plt.title('Line Plot')  # Adding a title
plt.xlabel('Time (hours)')  # Adding label for X-axis
plt.ylabel('Temperature (degrees)')  # Adding label for Y-axis
plt.legend()  # Show legend

# Creating a scatter plot
plt.subplot(1, 2, 2)  # Second plot in the 1 row, 2 column layout
plt.scatter(x, y_scatter, color='r', label='Speed')  # Plotting the scatter plot
plt.title('Scatter Plot')  # Adding a title
plt.xlabel('Time (hours)')  # Adding label for X-axis
plt.ylabel('Speed (km/h)')  # Adding label for Y-axis
plt.legend()  # Show legend

# Show the plots
plt.tight_layout()  # Adjust layout to make room for all elements
plt.show()  # Display the plot window
