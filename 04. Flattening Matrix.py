n = int(input())
print([int(el) for el in range(n) for el in input().split(", ")])