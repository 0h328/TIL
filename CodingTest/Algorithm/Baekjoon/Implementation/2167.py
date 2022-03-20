import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
K = int(sys.stdin.readline())
for _ in range(K):
    i, j, x, y = map(int, sys.stdin.readline().split())

    total = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            total += nums[a][b]

    print(total)
