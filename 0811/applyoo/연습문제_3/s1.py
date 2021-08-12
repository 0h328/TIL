import sys
sys.stdin = open('input.txt')

arr = list(map(int ,input().split()))

for i in range(1<<len(arr)):
    for j in range(len(arr)+1):
        if i & (1<<j): # i와 j 번째가 1인 비트(즉, j번째가 1인 i만 if문에 걸리게 됨)
            print(arr[j], end=' ')
    print()
print()