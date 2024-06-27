import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the points on the elliptic curve
def elliptic_curve(a, b, x_range):
    x = np.linspace(x_range[0], x_range[1], 1000)
    y_squared = x**3 + a*x + b
    y_squared[y_squared < 0] = np.nan  # Replace negative values with NaN
    y = np.sqrt(y_squared)
    return x, y, -y

# Elliptic curve parameters
a = -1
b = 1
x_range = (-2, 2)

# Calculate points
x, y1, y2 = elliptic_curve(a, b, x_range)

# Create a plot
fig, ax = plt.subplots()

# Plot the elliptic curve in black
ax.plot(x, y1, 'k')
ax.plot(x, y2, 'k')

# Add a single orange dot on the curve
valid_indices = np.where(~np.isnan(y1))[0]
mid_index = valid_indices[len(valid_indices) // 2]
ax.plot(x[mid_index], y1[mid_index], 'o', color='orange', markersize=12)

# Set plot limits
ax.set_xlim(x_range)
ax.set_ylim(-2, 2)

# Add x and y axes
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

# Remove ticks
ax.set_xticks([])
ax.set_yticks([])

# Save the plot as an SVG file
plt.savefig('elliptic_curve.svg', format='svg', bbox_inches='tight')

# Show the plot
plt.show()
