import sys

sys.stdin = open('input.txt')

T = int(input())

i = 1
while i <= T:
    ans = 0
    puzzle = []

    N, K = map(int, input().split())

    # puzzle로 배열을 만듦
    col = 0
    while col < N:
        tmp_list = list(map(int, input().split()))
        puzzle.append(tmp_list)
        col += 1

    # 가로를 계산
    for row in range(N):
        cnt = 0

        for col in range(N):
            if puzzle[row][col] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
            else:
                cnt += 1

        if cnt == K:
            ans += 1

    # 세로를 계산
    for col in range(N):
        cnt = 0

        for row in range(N):
            if puzzle[row][col] == 0:
                if cnt == K:
                    ans += 1
                cnt = 0
            else:
                cnt += 1

        if cnt == K:
            ans += 1

    print('#{} {}'.format(i, ans))

    i += 1