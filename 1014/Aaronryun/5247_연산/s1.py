import sys

sys.stdin = open('input.txt')
"""
연산이 앞에서부터 진행된다 -> 큐 사용
"""
from collections import deque

def sol(N):
    queu = deque()
    queu.append((N, 0))
    visit = set()
    visit.add(N)
    while queu:
        N, cnt = queu.popleft()
        if N == M:
            return cnt
        cal = [N + 1, N - 1, N * 2, N - 10]
        for i in cal:
            if i not in visit and i <= 1000000:
                queu.append((i, cnt + 1))
                visit.add(i)


for test in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    answer = sol(N)
    print('#{} {}'.format(test, answer))
