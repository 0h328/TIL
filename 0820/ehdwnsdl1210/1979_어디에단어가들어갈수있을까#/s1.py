import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N : 2차원 리스트 크기 / K : 내가 찾고 싶은 길이
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) + [0] for _ in range(N)]
    puzzle.append([0]*(N+1))    # 위에 + [0] 까지 포함해서 띄를 두르는!
    ans = 0

    for i in range(N):
        # 행 검사
        cnt_r = 0
        for j in range(N+1):
            if puzzle[i][j] == 1:   # 흰색이면
                cnt_r += 1
            else:
                # 벽이라면
                if cnt_r == K:
                    ans += 1
                cnt_r = 0
        # # 끝까지 가서야 완성이 된 경우
        # if cnt_r == K:
        #     ans += 1

        # 열 검사
        cnt_c = 0
        for j in range(N+1):
            if puzzle[j][i] == 1:
                cnt_c += 1
            else:
                if cnt_c == K:
                    ans += 1
                cnt_c = 0
        # if cnt_c == K:
        #     ans += 1

    print('#{} {}'.format(tc, ans))
'''
    # 가로
    for i in range(len(arr)):
        for j in range(N-K+1):
            if sum(arr[i][j:j+N-K+1]) == K:
                cnt += 1

    # 세로(회전하고 가로 검사)
    for i in range(N-K+1):
        for j in range(len(arr)):
            if sum(arr[j][i]) == K:
                cnt += 1

    print('#{} {}'.format(tc, cnt))
'''
# 빈칸에서 벽으로? while?
# 끝났을 때도? K?
# 오른쪽/밑 각각 끝에 벽을 두면????  마지막 도착 조건 안줘도...
# 띄를 만들면 전치행렬로 하면 세로도 가능
