import sys
sys.stdin = open('input.txt')

# 2. (수업) 테두리에 벽 만들기
T = int(input())

for t in range(1, T+1):
    # N: 2차원리스트의 크기, K: 내가 찾고 싶은 길이
    N, K = map(int, input().split())

    # 테두리 벽
    puzzle = [list(map(int, input().split())) + [0] for _ in range(N)]
    puzzle.append([0] * (N+1))

    ans = 0

    for i in range(N):
        # 행 검사
        cnt_r = 0
        for j in range(N+1):
            if puzzle[i][j] == 1: # 흰색
                cnt_r += 1
            else: # 벽
                if cnt_r == K:
                    ans += 1
                cnt_r = 0

        # 열 검사
        cnt_c = 0
        for j in range(N+1):
            if puzzle[j][i] == 1:
                cnt_c += 1
            else:
                if cnt_c == K:
                    ans += 1
                cnt_c = 0

    print('#{} {}'.format(t, ans))