# Reimport necessary libraries after the reset
import numpy as np
import matplotlib.pyplot as plt

FONT_SIZE = 26

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))

# Define the "puddle" shape (Omega boundary)
theta = np.linspace(0, 2 * np.pi, 500)
r = 1 + 0.2 * np.sin(3 * theta) + 0.1 * np.cos(5 * theta)
x = r * np.cos(theta)
y = r * np.sin(theta)
ax.plot(x, y, color='black', linewidth=2, label=r'$\Gamma$')  # Omega boundary

# Fill the interior of the "puddle" (Omega)
ax.fill(x, y, color='lightblue', alpha=0.5, label=r'$\Omega$')

# Add two subregions G_1 and G_2
circle1 = plt.Circle((-0.3, 0.2), 0.3, edgecolor='blue', facecolor='white', linewidth=2, label=r'$G_1$')
circle2 = plt.Circle((0.2, -0.7), 0.3, edgecolor='red', facecolor='white', linewidth=2, label=r'$G_2$')
ax.add_patch(circle1)
ax.add_patch(circle2)

# Label the regions
ax.text(-0.3, 0.2, r'$\Gamma_2$', ha='center', va='center', fontsize=FONT_SIZE, color='black')  # In G_1
ax.text(0.2, -0.7, r'$\theta_*$', ha='center', va='center', fontsize=FONT_SIZE, color='red')   # In G_2

# Add a label for the boundary Gamma
ax.text(0.7, -0.9, r'$\Gamma$', fontsize=FONT_SIZE, color='black', ha='center', va='center')
ax.text(0.5, 0.2, r'$\Omega$', fontsize=FONT_SIZE, color='black', ha='center', va='center')

# Set the limits and aspect
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Display the plot
plt.legend(loc='upper right', fontsize=FONT_SIZE, frameon=False)
plt.savefig('omega-g1-g2.eps', bbox_inches='tight', pad_inches=0)
plt.savefig('omega-g1-g2.png', bbox_inches='tight', pad_inches=0)
