import sys
sys.stdin = open('input.txt')

l = input().split()
length = len(l)
for i in range(1 << length):
    for j in range(length + 1):
        if i & (1 << j):
            print(l[j], end=' ')
    print()
