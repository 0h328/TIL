import sys
from collections import deque

sys.stdin = open('input.txt')
'''
자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.
단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.
'''

def my_calc(num, calc):
    if calc == 0:
        return num + 1
    elif calc == 1:
        return num - 1
    elif calc == 2:
        return num * 2
    elif calc == 3:
        return num - 10


def bfs(N, M):
    Q = deque()
    Q.append((N, 0))
    visited[N] = 1
    while Q:
        num, cnt = Q.popleft()
        for i in range(4):
            next_num = my_calc(num, i)
            if next_num == M:  # 최소 거리로 M이 되는 순간 return
                return cnt + 1
            elif 0 < next_num <= 1000000 and not visited[next_num]:  # not visited 필수
                Q.append((next_num, cnt + 1))
                visited[next_num] = 1

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * 1000001  # 100만 포함해야 함
    print('#{} {}'.format(t, bfs(N, M)))