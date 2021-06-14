def is_valid(r,c):
    if 0 > r or 0 > c or r > (len(matrix)-1) or c > (len(matrix)-1):
        return False
    return True

matrix = [[int(el) for el in input().split()]for _ in range(int(input()))]

command = input()
while not command == "END":
    command_type, row , col , value = command.split()
    row , col , value = int(row) , int(col), int(value)
    if is_valid(row, col):
        if command_type == "Add":
            matrix[row][col] += value
        elif command_type == "Subtract":
           matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    command = input()

print('\n'.join(' '.join([str(el) for el in r])for r in matrix))