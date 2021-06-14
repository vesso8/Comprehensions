# row, col = input().split()
# row , col = int(row), int(col)
# matrix = []
#
# first_char = ord('a')
# for r in range(row):
#     matrix.append([])
#     for c in range(col):
#         first_element = chr(r + first_char)
#         middle_element = chr(r + c + first_char)
#         matrix[-1].append(f'{first_element}{middle_element}{first_element}')
#
# print('\n'.join(' '.join([str(el) for el in r])for r in matrix))
def generate_elements(r, c):
    first_char = ord('a')
    first_element = chr(r + first_char)
    middle_element = chr(r + c + first_char)
    return f'{first_element}{middle_element}{first_element}'

n , m = input().split()
n , m = int(n), int(m)

matrix = [[generate_elements(row, col) for col in range(m)] for row in range(n)]

print('\n'.join(' '.join([str(el) for el in r])for r in matrix))
