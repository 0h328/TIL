import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(n):
    que = deque()
    que.append((n, 0)) # 현재 값, 연산 수
    visited.add(n)
    while que:
        n, cnt = que.popleft()
        if n == m:
            return cnt
        cal = [n + 1, n - 1, n * 2, n - 10]
        for i in cal:
            if i not in visited and i <= 1000000:
                que.append((i, cnt + 1))
                visited.add(i)

for tc in range(int(input())):
    n, m = map(int, input().split())
    visited = set()
    print('#{} {}'.format(tc+1, bfs(n)))



'''
def bfs(n):
    que = deque()
    que.append((n, 0)) # 현재 값, 연산 수
    visited.add(n)
    while que:
        n, cnt = que.popleft()
        if n == m:
            return cnt
        if n+1 not in visited and n + 1 <= 1000000:
            que.append((n + 1, cnt + 1))
            visited.add(n+1)
        if n-1 not in visited and 1 <= n - 1 <= 1000000:
            que.append((n - 1, cnt + 1))
            visited.add(n - 1)
        if n*2 not in visited and n * 2 <= 1000000:
            que.append((n * 2, cnt + 1))
            visited.add(n * 2)
        if n-10 not in visited and 1 <= n - 10 <= 1000000:
            que.append((n - 10, cnt + 1))
            visited.add(n - 10)

for tc in range(int(input())):
    n, m = map(int, input().split())
    visited = set()
    print('#{} {}'.format(tc+1, bfs(n)))
'''