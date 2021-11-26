import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    # 가로 방향. 0이나 범위 끝 도달하면 이전에 센 cnt 값 판단
    for row in range(N):
        cnt = 0
        for col in range(N):
            if total_map[row][col] == 1:
                cnt += 1
            if total_map[row][col] == 0 or col == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0
    # 세로 방향
    for col in range(N):
        cnt = 0
        for row in range(N):
            if total_map[row][col] == 1:
                cnt += 1
            if total_map[row][col] == 0 or row == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0

    print('#{} {}'.format(tc, ans))