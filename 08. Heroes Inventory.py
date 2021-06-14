names = input().split(", ")
command = input()
collection = {name: {} for name in names}
while not command == "End":
    name , item , cost = command.split("-")
    if not collection[name].get(item):
        collection[name].update({item:int(cost)})
    command = input()
print(*[f"{name} -> Items: {len(inventory)}, Cost: {sum([inventory[item] for item in inventory])}" for name, inventory in collection.items()], sep="\n")