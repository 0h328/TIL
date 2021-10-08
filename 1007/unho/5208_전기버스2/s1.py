import sys
sys.stdin = open('input.txt')


def bfs(idx, ans):
    global answer

    if idx >= N-1:              # 도착지 도착 or 도착지 넘어서 도착하면
        if answer > ans:
            answer = ans
        return
    elif ans >= answer:         # 중간에 최소 배터리 교체 횟수 넘어가면
        return

    for i in range(station[idx], 0, -1):    # 멀리가는 경우부터 순회
        bfs(idx+i, ans+1)


T = int(input())

for tc in range(1, T+1):
    N, *station = map(int, input().split())
    answer = 1e10

    bfs(0, -1)          # BFS 탐색

    print('#{} {}'.format(tc, answer))