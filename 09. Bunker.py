bunker = {categories: [] for categories in input().split(", ")}

n = int(input())
bunker['all_items_count'] = 0
bunker['average_quality'] = 0
for _ in range(n):
    items , materials, item_q = input().split(" - ")
    item_quantity = int(item_q.split(";")[0].split(":")[1])
    item_quality = int(item_q.split(";")[1].split(":")[1])
    item_data = {materials: {'quantity':item_quantity , 'quality': item_quality}}
    bunker[items].append(item_data)
    bunker['all_items_count'] += item_quantity
    bunker['average_quality'] += item_quality

print(f"Count of items: {bunker['all_items_count']}")
print(f"Average quality: {(bunker['average_quality']/(len(bunker)-2)):.2f}")
print(*[f"{category} -> {', '.join([list(d.keys())[0] for d in value])}" for category , value in bunker.items() if isinstance(bunker[category],list)], sep='\n')