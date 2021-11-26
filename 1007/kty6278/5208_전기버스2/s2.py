# 상훈님 코드인데 너무 좋다
import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        v = queue.popleft()
        for w in arr[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = visited[v] + 1


T = int(input())

for test_case in range(1, T+1):
    nums = list(map(int, input().split()))
    N = nums[0]
    charges = [0] + nums[1:]
    arr = [[] for _ in range(N+1)]
    for i in range(1, N):
        for j in range(1, charges[i]+1):
            if i+j > N:
                arr[i].append(N)
            else:
                arr[i].append(i+j)

    visited = [0] * (N+1)
    bfs(1)
    ans = visited[N]-2

    print('#{} {}'.format(test_case, ans))