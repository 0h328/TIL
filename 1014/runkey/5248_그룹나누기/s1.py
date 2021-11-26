import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(i):
    stack = deque()
    stack.append(i)
    while stack:
        x = stack.popleft()
        if not visited[x]:
            visited[x] = 1
            for y in N_list[x]:
                stack.append(y)

tc = int(input())
for t in range(1, tc + 1):
    result = 0
    N, M = map(int, input().split())
    N_list = [[] for _ in range(N + 1)]
    temp = list(map(int, input().split()))
    visited = [0] * (N + 1)
    for m in range(M):
        N_list[temp[2 * m]].append(temp[2 * m + 1])
        N_list[temp[2 * m + 1]].append(temp[2 * m])
    print(N_list)

    for i in range(1, N + 1):
        if not visited[i]:
            bfs(i)
            print(visited)
            result += 1
    print("#{} {}".format(t, result))