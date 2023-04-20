from collections import Counter

strings = ["bella", "label", "roller"]

# Подсчитываем количество вхождений каждой буквы во всех строках
counts = Counter("".join(strings))

# Отбираем только те буквы, которые встречаются во всех строках
result = [char for char, count in counts.items() if count == len(strings)]

print(result)