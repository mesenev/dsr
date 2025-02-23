import matplotlib.pyplot as plt
import matplotlib.patches as patches
FONT_SIZE = 26
FONT_SIZE_2 = 20

# Создаем фигуру и оси
fig, ax = plt.subplots(figsize=(6, 6))

# Рисуем квадрат (\Gamma_1)
square = patches.Rectangle((-1, -1), 2, 2, edgecolor='black', facecolor='none', linewidth=2, label=r'$\Gamma_1$')
ax.add_patch(square)

# Рисуем круг (\Gamma_2)
circle = patches.Circle((0, 0), 0.5, edgecolor='black', facecolor='white', linewidth=2, label=r'$\Gamma_2$')
ax.add_patch(circle)
ax.text(-0.2, 0.2, r'$\Gamma_2$', ha='center', va='center', fontsize=FONT_SIZE, color='black')  # In G_1
ax.text(-0.1, -0.1, r'$q_b, \gamma-?$', ha='center', va='center', fontsize=FONT_SIZE_2, color='blue')  # In G_1
ax.text(-1, 1.12, r'$\Gamma_1$', ha='center', va='center', fontsize=FONT_SIZE, color='black')   # In G_2
ax.text(-0.3, 1.12, r'$q_b, \theta_b, \gamma$', ha='center', va='center', fontsize=FONT_SIZE_2, color='blue')   # In G_2
ax.text(0.2, -0.7, r'$\Omega$', ha='center', va='center', fontsize=FONT_SIZE, color='black')   # In G_2

# Настройка отображения
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')
# Подписи и легенда
ax.set_xlabel('x')
ax.set_ylabel('y')

# Показываем результат
plt.grid(visible=False)
plt.savefig('omega-circle.png', bbox_inches='tight',)
plt.savefig('omega-circle.eps', bbox_inches='tight' )
