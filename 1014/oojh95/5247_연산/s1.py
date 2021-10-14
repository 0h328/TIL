import sys
sys.stdin = open('input.txt')


def bfs(n, cnt):
    global result
    stack.append((n, cnt))
    while stack:
        (a, b) = stack.pop(0)
        if a == M:
            result = b
            break
        stack.append((a * 2, b + 1))
        stack.append((a+1, b+1))
        stack.append((a - 1, b + 1))
        stack.append((a - 10, b + 1))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    stack = []
    result = 1000000
    bfs(N, 0)
    print('#{} {}'.format(tc, result))