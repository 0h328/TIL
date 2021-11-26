"""
- append, pop(0) 연산을 통해서 구현하는 경우 시간 초과 가능성
- deque을 사용하거나 Queue의 사이즈를 설정하고 front, rear 포인터를 활용하는 방식으로 해결
"""
def bfs(N, M):
    front = rear = -1                                           # 포인터 초기화
    visited[N] = 1                                              # 방문 기록
    rear += 1                                                   # 초기값 -> enQueue 연산을 위해 rear를 하나 증가 시키고
    Q[rear] = N                                                 # 큐에 시작 노드 인큐

    """
    일반적인 Q -> while Q:
    포인터를 활용한 Q -> rear == front? Q가 비었다!
    """
    while front != rear:                                        # 큐가 비어있지 않으면(=> while Q:)
        front += 1                                              # deQueue -> Queue에서 값을 가져오기 위해 1 증가
        cur_n = Q[front]                                        # 다음 노드를 꺼내 그걸 현재 num으로 두고
        calc_nums = [cur_n+1, cur_n-1, cur_n*2, cur_n-10]       # 인접 노드번호 계산하기 위한 리스트 초기화 (사용 가능한 연산)

        for i in range(4):                                      # 4번 연산을 수행하며
            if calc_nums[i] == M:                               # 찾는 노드인 경우(연산 결과인 경우)
                return visited[cur_n]                           # 거리 리턴(최소 연산 횟수)

            if 0 < calc_nums[i] <= 1000000:                     # 유효한 노드 번호이고
                if not visited[calc_nums[i]]:                   # 아직 방문하지 않은 노드면
                    visited[calc_nums[i]] = visited[cur_n] + 1  # 거리를 기록하고(연산 횟수 누적)
                    rear += 1                                   # 포인터 옮기고
                    Q[rear] = calc_nums[i]                      # Q에 추가

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())                            # N을 M으로 바꾸는 최소한의 연산 횟수(M은 100만 이하의 자연수)
    Q = [0] * 1000000
    visited = [0 for _ in range(1000001)]
    print('#{} {}'.format(tc, bfs(N, M)))