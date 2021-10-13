import sys
sys.stdin = open('input.txt')


def search(num):
    global tc_answer

    for k in linked[num]:           # 연결된것들 이어서 탐색
        if not visited[k]:          # 방문하지 않았으면
            visited[k] = 1          # 방문으로 체크
            search(k)               # 탐색
            visited[k] = 0          # 방문하지 않은걸로 원상복구

    if tc_answer < sum(visited):    # 가장 많이 방문한거로 갱신
        tc_answer = sum(visited)


T = int(input())
answer = []

for tc in range(1, T+1):
    N, M = map(int, input().split())
    linked = {i: [] for i in range(1, N+1)}
    visited = [0] * (N+1)
    tc_answer = 1

    for _ in range(M):                      # 연결관계 생성
        x, y = map(int, input().split())
        linked[x].append(y)
        linked[y].append(x)

    for i in range(1, N+1):                 # 모든 노드들을 시작점으로 해봄
        search(i)

    answer.append('#{} {}'.format(tc, tc_answer))

print(*answer, sep='\n')