points = [(1, 10), (2, 5), (3, 8)]
# Сортируем по второму элементу (10, 5, 8)
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)  # [(2, 5), (3, 8), (1, 10)]