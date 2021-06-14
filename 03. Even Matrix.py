def even_nums(number):
    if number % 2 == 0:
        return True
    return False
n = int(input())
matrix = [[int(el) for el in input().split(", ")]for _ in range(n)]
even_matrix = [[num for num in sublist if even_nums(num)] for sublist in matrix]
print(even_matrix)