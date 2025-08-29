# Import the pyplot module from Matplotlib, commonly abbreviated as plt
import matplotlib.pyplot as plt

# Data for the plots
x = [1, 2, 3, 4, 5]  # Example data for X-axis
y1 = [2, 3, 2, 5, 7]  # Y-axis data for the first subplot (e.g., temperature in Celsius)
y2 = [1, 2, 1, 2, 1]  # Y-axis data for the second subplot (e.g., rainfall in cm)

# Create a figure and a set of subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))  # 2 rows, 1 column, figure size 8x6 inches

# First subplot
ax1.plot(x, y1, 'r-o')  # Red line with circle markers
ax1.set_title('Temperature over Days')  # Title for the first subplot
ax1.set_xlabel('Day')  # X-axis label for the first subplot
ax1.set_ylabel('Temperature (Celsius)')  # Y-axis label for the first subplot

# Second subplot
ax2.plot(x, y2, 'b--o')  # Blue dashed line with circle markers
ax2.set_title('Rainfall over Days')  # Title for the second subplot
ax2.set_xlabel('Day')  # X-axis label for the second subplot
ax2.set_ylabel('Rainfall (cm)')  # Y-axis label for the second subplot

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the figure
plt.show()
