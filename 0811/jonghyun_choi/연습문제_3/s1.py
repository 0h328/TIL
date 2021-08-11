import sys
sys.stdin = open('input.txt')

arr = list(map(int,input().split()))
n = len(arr)

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=' ')
    print()
print()