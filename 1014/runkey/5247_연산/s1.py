import sys
sys.stdin = open('input.txt')

from collections import deque
sys.setrecursionlimit(10 ** 6)
def cnt(n, plus):
    global result
    stack = deque()
    stack.append((n, plus))

    while stack:
        n, plus = stack.pop()
        for i in range(4):
            if i == 0:
                m = n + 1
            if i == 1:
                m = n - 1
            if i == 2:
                m = n * 2
            if i == 3:
                m = n - 10
            if n == M:
                if result > plus:
                    result = plus
                return

            if i == 0 and m not in visited and 0 < n + 1 <= 1000000:
                stack.append((n + 1, plus + 1))
                visited.add(n + 1)
            if i == 1 and n not in visited and 0 < n - 1 <= 1000000:
                stack.append((n - 1, plus + 1))
                visited.add(n - 1)
            if i == 2 and n not in visited and 0 < n * 2 <= 1000000:
                stack.append((n * 2, plus + 1))
                visited.add(n * 2)
            if i == 3 and n not in visited and 0 < n - 10 <= 1000000:
                stack.append((n - 10, plus + 1))
                visited.add(n - 10)

tc = int(input())
result = 1e9
flag = 0
for t in range(1, tc + 1):
    N, M = map(int, input().split())
    visited = set()
    cnt(N, 0)
    print("{} {}".format(t, result))