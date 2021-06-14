n = int(input())
matrix = [[int(el) for el in input().split(", ")]for _ in range(n)]

first_diagonal = [matrix[row][row] for row in range(n)]
second_diagonal = [matrix[row][n-1-row] for row in range(n)]

print(f"First diagonal: {', '.join([str(x) for x in first_diagonal])}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join([str(x) for x in second_diagonal])}. Sum: {sum(second_diagonal)}")
