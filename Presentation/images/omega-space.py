import matplotlib.pyplot as plt

FONT_SIZE = 26
fig, ax = plt.subplots(figsize=(6, 6))
ax.plot([0, 0], [0, 1], color='black', linewidth=2)
ax.plot([1, 1], [0, 1], color='black', linewidth=2)
x_top = [i / 100 for i in range(101)]
y_top = [1 + 0.02 * (i % 2) for i in range(101)]
ax.plot(x_top, y_top, color='black', linewidth=2)
ax.plot([0, 1], [0, 0], color='black', linewidth=2, linestyle='--')
ax.text(0.5, 1.05, r'$\Gamma_2, \theta = \theta_0$', ha='center', va='bottom', fontsize=FONT_SIZE)
ax.text(0.5, -0.05, r'$\Gamma_1, u - ?$', ha='center', va='top', fontsize=FONT_SIZE)
ax.text(-0.05, 0.5, r'$\Gamma_0$', ha='center', va='bottom', fontsize=FONT_SIZE)
ax.text(1.05, 0.5, r'$\Gamma_0$', ha='center', va='bottom', fontsize=FONT_SIZE)
# ax.set_xlim(-0.2, 1.2)
ax.axis('off')
plt.savefig(
    'omega_1.png',
    bbox_inches='tight'
)
