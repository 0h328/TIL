import sys

sys.stdin = open('input.txt')

data = list(map(int, input().split()))

for i in range(1 << len(data)):
    for j in range(len(data)):
        if i & (1 << j):
            print(data[j], end=' ')
    print()
