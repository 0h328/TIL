import sys
sys.stdin = open('input.txt')

lst = list(map(int, input().split()))

for i in range(1, 1<< len(lst)):
    for j in range(len(lst)):
        if i & (1 << j):
            print(lst[j], end=' ')
    print()