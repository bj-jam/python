vec = [2, 4, 6]
v = [3 * x for x in vec]
print(v)
v = [[x, x ** 2] for x in vec]
print(v)
v = [3 * x for x in vec if x > 3]
print(v)

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
dd = [weapon.strip() for weapon in freshfruit]
print(dd)

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
v = [x * y for x in vec1 for y in vec2]
print(v)  # [8, 6, -18, 16, 12, -36, 24, 18, -54]

v = [x + y for x in vec1 for y in vec2]
print(v)  # [6, 5, -7, 8, 7, -5, 10, 9, -3]
v = [vec1[i] * vec2[i] for i in range(len(vec1))]
print(v)  # [8, 12, -54]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

v = [[row[i] for row in matrix] for i in range(4)]
print(v)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

v = []
for i in range(4):
    v.append([row[i] for row in matrix])
print(v)

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    # What is your name?  It is lancelot.
    # What is your quest?  It is the holy grail.
    # What is your favorite color?  It is blue.
    print('What is your {0}?  It is {1}.'.format(q, a))

from course10 import fib

fib(50)
