import sys
from collections import deque
sys.stdin = open("input.txt")

T = int(input())

def bfs(root):
    queue = deque()
    queue.append(root)
    visited[root] = 1
    cnt = 1

    while queue:
        cur = queue.popleft()
        for nxt in tree[cur]:
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = 1
                cnt += 1
    return cnt


for tc in range(1, T+1):
    E, N = map(int, input().split())

    tree = [[] for _ in range(E+2)]
    data = list(map(int, input().split()))

    for i in range(E):
        parent, child = data[2*i], data[2*i+1]

        tree[parent].append(child)

    visited = [0 for _ in range(E+2)]
    ans = bfs(N)
    print("#{} {}".format(tc, ans))