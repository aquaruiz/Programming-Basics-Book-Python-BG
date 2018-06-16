# # Правоъгълник от 10 x 10 звездички
# for i in range(10):
#     print('*' * 10)

# # Правоъгълник от N x N звездички
# n = int(input())
# for i in range(n):
#     print('*' * n)

# # Квадрат от звездички
# n = int(input())
# for row in range(n):
#     for col in range(n):
#         print('* ', end='')
#     print()

# # Триъгълник от долари
# n = int(input())
# for row in range(n):
#     print('$', end='')
#     for col in range(row):
#         print(' $', end='')
#     print()

# # Квадратна рамка
# n = int(input())
# print('+', end='')
# for i in range(n - 2):
#     print(' -', end='')
# print(' +')

# for row in range(n - 2):
#     print('|', end='')
#     for col in range(n - 2):
#         print(' -', end='')
#     print(' |')
    
# print('+', end='')
# for i in range(n - 2):
#     print(' -', end='')
# print(' +')

# # Ромбче от звездички
# n = int(input())
# for row in range(1, n + 1):
#     print(' ' * (n - row), end='')
#     print('*', end='')
#     print(' *' * (row - 1))

# for row in reversed(range(1, n)):
#     print(' ' * (n - row), end='')
#     print('*', end='')
#     print(' *' * (row - 1))

# # Коледна елха
# n = int(input())
# for i in range(n + 1):
#     print(' ' * (n - i), end='')
#     print('*' * i, end='')
#     print(' | ', end='')
#     print('*' * i, end='')
#     print()

# # Слънчеви очила
# n = int(input())
# print('*' * (2 * n), end='')
# print(' ' * n, end='')
# print('*' * (2 * n))

# for i in range(n - 2):
#     print('*', end='')
#     print('/' * (2 * n - 2), end='')
#     print('*', end='')
#     if i == (n-1) // 2 - 1:
#         print('|' * n, end='')
#     else:    
#         print(' ' * n, end='')
#     print('*', end='')
#     print('/' * (2 * n - 2), end='')
#     print('*')


# print('*' * (2 * n), end='')
# print(' ' * n, end='')
# print('*' * (2 * n))

# # Къщичка
# n = int(input())
# countOfStars = 2 if n % 2 == 0 else 1
# countOfDashes = (n - countOfStars) // 2 # ternary operator

# for i in range((n + 1) // 2):
#     print('-' * countOfDashes, end='')
#     print('*' * countOfStars, end='')
#     print('-' * countOfDashes)
#     countOfDashes -= 1
#     countOfStars += 2

# for j in range(n // 2):
#     print('|' + '*' * (n - 2) + '|')

# Диамант
n = int(input())
countOfStarts = 2 if n % 2 == 0 else 1
countOfDashes = (n - 1) // 2
if n < 3:
    print('*' * countOfStarts)
else:
    print('-' * countOfDashes, end='')
    print('*' * countOfStarts, end='')
    print('-' * countOfDashes)
    middleDashes = countOfStarts

    for row in range((n - 1) // 2):
        countOfDashes -= 1
        print('-' * countOfDashes, end='')
        print('*', end='')
        print('-' * middleDashes, end='')
        print('*', end='')        
        print('-' * countOfDashes)
        middleDashes += 2

    middleDashes -= 4

    for row in range((n - 1) // 2 - 1):
        countOfDashes += 1
        print('-' * countOfDashes, end='')
        print('*', end='')
        print('-' * middleDashes, end='')
        print('*', end='')
        print('-' * countOfDashes)
        middleDashes -= 2

    countOfDashes += 1
    print('-' * countOfDashes, end='')
    print('*' * countOfStarts, end='')
    print('-' * countOfDashes)