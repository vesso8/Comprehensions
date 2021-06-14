cities = input().split(", ")
capitals = input().split(", ")

text = {cities[index]:capitals[index] for index in range(len(cities))}
print('\n'.join([f"{key} -> {value}" for key, value in text.items()]))