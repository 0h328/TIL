import sys
sys.stdin = open('input.txt')

# N = int(input())
arr = list(map(int, input().split()))
N = len(arr)
for i in range(1, 1<<N): # 2의 N승
    for j in range(N):
        if i & (1<<j):
            print(arr[j], end=' ')
    print()

