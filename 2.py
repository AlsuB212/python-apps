a = [1, 4, 6]
b = [11, 33, 22]

# Создаем список пар, где первый элемент - элемент второго списка b, а второй элемент - соответствующий элемент из первого списка a
pairs = [(b[i], a[i]) for i in range(len(a))]

# Сортируем список пар по первому элементу (элементам второго списка b)
sorted_pairs = sorted(pairs, key=lambda x: x[0])

# Извлекаем второй элемент из каждой пары, который соответствует элементам первого списка a
a_sorted = [pair[1] for pair in sorted_pairs]

print(a_sorted)