import sys
<<<<<<< HEAD
from collections import deque
=======
>>>>>>> 0f3d00a6e1043fba483b14d316abf1af9418f6a3
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    containers.sort()
    trucks.sort(reverse=True)

    ans = 0
    for truck in trucks:
        while containers:
            cur = containers.pop()
            if truck < cur:
                continue
            else:
                ans += cur
                break

    print('#{} {}'.format(tc, ans))
