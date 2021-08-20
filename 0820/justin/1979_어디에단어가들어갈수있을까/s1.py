import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):                          # 행
        cnt = 0
        for j in range(1, N):                   # 1부터 도는 것은 index 연산 때문
            if data[i][j-1] == data[i][j] == 1: # 현재와 그 다음이 1 이면
                cnt += 1                        # 1 카운트
            else:                               # 1이 아닌 경우
                if cnt == K-1:                  # 이때 K-1번 돌았다면
                    ans += 1                    # 현재 K-1번 카운트가 되었으므로 체크 (0부터 시작했기 때문)
                cnt = 0
        if cnt == K-1:                          # 만약 다 돌고 K-1번 이라면
            ans += 1                            # 이것도 체크

    for i in range(N):                          # 열
        cnt = 0
        for j in range(1, N):
            if data[j-1][i] == data[j][i] == 1:
                cnt += 1
            else:
                if cnt == K-1:
                    ans += 1
                cnt = 0
        if cnt == K-1:
            ans += 1
    print('#{} {}'.format(tc, ans))