import sys

sys.stdin = open('input.txt')

T = int(input())

data = []
for test in range(T):
    data.append(list(map(int, input().split())))

for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end=' ')
print()

for i in range(len(data[0])):
    for j in range(len(data)):
        print(data[j][i], end=' ')
print()

for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j + ((len(data[i]) - 1) - 2 * j) * (i % 2)], end=' ')
print()

for i in range(len(data)):
    for j in range(len(data[i])):
        if i < j:
            data[i][j], data[j][i] = data[j][i], data[i][j]
print(data)
