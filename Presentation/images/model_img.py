import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Создаем фигуру и ось
fig, ax = plt.subplots(figsize=(6,6))

# Определим произвольную замкнутую область Omega (в виде многоугольника)
points = [(2, 1), (5, 1.5), (6, 3), (4.5, 5), (2.5, 4), (1.5, 2.5)]
omega_polygon = patches.Polygon(points, closed=True, edgecolor='black',
                                  linewidth=2, facecolor='lightblue')
ax.add_patch(omega_polygon)

# Подпишем внешнюю область (например, разместив текст вне Omega)
ax.text(0.5, 5.5, "Внешняя среда:\n$\\theta_{out}$", fontsize=18,
        color="blue", bbox=dict(facecolor='none', edgecolor='blue', boxstyle='round'))

# Найдем приблизительный центр многоугольника для размещения внутренних подписей
centroid_x = sum([p[0] for p in points]) / len(points)
centroid_y = sum([p[1] for p in points]) / len(points)

# Внутри Omega подпишем состояние и параметры
ax.text(centroid_x, centroid_y+0.5, "Состояние:\n$\\theta$, $\\varphi$", fontsize=18, ha="center")
ax.text(centroid_x, centroid_y-0.5, "Параметры среды:\n$a$, $b$, $\\kappa_a$, $\\alpha$",
        fontsize=18, ha="center", color="darkgreen")

# На границе области пометим граничные условия.
# Определим точку с максимальной y (верхняя граница)
max_y_point = max(points, key=lambda p: p[1])
ax.text(max_y_point[0], max_y_point[1]+0.2,
        "Граничные параметры:\n$\\beta$, $\\gamma$, $\\partial_n \\theta$, $\\theta_b$", fontsize=18,
        color="red", ha="center")

# Вычислим минимальные и максимальные значения по x и y
xs = [p[0] for p in points]
ys = [p[1] for p in points]
margin = 0.2  # минимальный отступ

ax.set_xlim(min(xs) - margin, max(xs) + margin)
ax.set_ylim(min(ys) - margin, max(ys) + margin)

ax.set_aspect('equal')
ax.axis('off')

# Сохраним изображение
plt.savefig('model_.png', bbox_inches='tight')
plt.savefig('model.eps', bbox_inches='tight')
