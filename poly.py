import numpy as np
import matplotlib.pyplot as plt

NUM_POINTS = 9

# Define the x and y values for the 8 points
x_points = np.arange(1, NUM_POINTS + 1)
y_points = np.random.randint(-5, 6, size=NUM_POINTS)


# Fit a degree 8 polynomial to the points
coefficients = np.polyfit(x_points, y_points, NUM_POINTS)
polynomial = np.poly1d(coefficients)

# Generate x values for plotting the polynomial
x_plot = np.linspace(-100, NUM_POINTS + 100, 10000)
y_plot = polynomial(x_plot)

# Create a plot
fig, ax = plt.subplots()

# Plot the polynomial curve in black
ax.plot(x_plot, y_plot, 'k')

# Add the original 8 points in orange
ax.plot(x_points, y_points, 'o', color='orange', markersize=10)

# Set plot limits
ax.set_xlim(0,  NUM_POINTS + 1)
ax.set_ylim(-10, 18)

# Add x and y axes
# ax.axhline(0, color='black', linewidth=0.5)
# ax.axvline(0, color='black', linewidth=0.5)

# Remove ticks
ax.set_xticks([])
ax.set_yticks([])

# Save the plot as an SVG file
plt.savefig('degree_8_polynomial.svg', format='svg', bbox_inches='tight')

# Show the plot
plt.show()
