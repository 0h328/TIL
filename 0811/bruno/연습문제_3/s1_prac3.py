import sys
sys.stdin = open('input.txt')

inp = list(map(int, input().split()))
N = len(inp)
for i in range(1, 1 << N):
    for j in range(N):
        if i & (1 << j):
            print(inp[j], end=' ')
    print()
print() # 공집합