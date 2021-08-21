import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # N : 2차원 리스트의 크기, K : 내가 찾고 싶은 길이
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
    # 행을 검사
        cnt_r = 0
        for j in range(N):
            if puzzle[i][j] == 1:   # 흰색부분이야
                cnt_r += 1
            else:
                # 벽이라면
                if cnt_r == K:
                    ans += 1
                cnt_r = 0
        # 끝까지 가서야 완성이 된 경우
        if cnt_r == K:
            ans += 1

        # 열을 검사
        cnt_c = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt_c += 1
            else:
                if cnt_c == K:
                    ans += 1
                cnt_c = 0
        if cnt_c == K:
            ans += 1
    print('#{} {}'.format(tc, ans))