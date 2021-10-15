# 연산을 위한 함수
def calc(num, idx):
    if idx == 0:
        return num + 1
    elif idx == 1:
        return num - 1
    elif idx == 2:
        return num * 2
    else:
        return num - 10

# 최소한의 연산 수행 -> BFS
"""
- 단순하게 append, pop(0) 연산을 통해서 구현하는 경우 시간 초과
- deque을 사용하거나 Queue의 사이즈를 100만 정도로 잡고 front, rear 포인터를 이동해서 접근
"""
def bfs():
    Q = [0] * 1000000
    front = rear = -1
    rear += 1                                                   # 초기값 -> enQueue 연산은 rear를 하나 증가 시키고 값을 넣는다.
    Q[rear] = (N, 0)                                            # 0은 몇 번 연산을 했는지 체크
    memo[N] = 0
    """
    일반적인 Q 사용 -> while Q:
    포인터 Q 사용 -> rear == front가 같아지면 Q가 빈 것
    """
    while front != rear:                                        # Queue가 비기 전까지
        front += 1                                              # deQueue -> Queue에서 값을 가져오기 위해 1 증가
        cur_n, cur_cnt = Q[front]                               # 현재 number, 현재 cnt를 Q에서 가져오기 (시작은 N, 0)
        if cur_n == M:                                          # N이 M이면 현재 count한 값을 반환
            return cur_cnt
        for i in range(4):                                      # 아닐 경우 4가지 연산 수행
            next_n = calc(cur_n, i)                             # next_n -> 다음 값
            if 0 < next_n <= 1000000 and memo[next_n] == -1:    # memo[next_n] == -1 -> 중복 연산 방지 (이미 값이 있는 경우는 연산이 완료된 케이스)
                memo[next_n] = memo[cur_n] + 1                  # 다음 값은 현재 값에서 1을 더한 것
                rear += 1
                Q[rear] = (next_n, cur_cnt+1)                   # next_n은 현재 한번 더 연산을 했다는 의미 -> cur_cnt + 1
    return memo[M]

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())                            # N을 M으로 바꾸는 최소한의 연산수
    memo = [-1] * 100000                                        # 10000001인 이유 -> 1 ~ 100만까지 사용 가능하기 때문
    print('#{} {}'.format(tc, bfs()))