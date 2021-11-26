import sys
import collections


sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case+1):
    N, M = map(int, input().split())
    q = collections.deque(map(int, input().split()))    # deque 에 할당

    for _ in range(M):
        q.append(q.popleft())                           # 왼쪽꺼 꺼내서 오른쪽에 붙임

    answer = q.popleft()

    print('#{} {}'.format(tc, answer))