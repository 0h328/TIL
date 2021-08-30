import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for i in range(N)]
    # print(flag)

    White = [0] * N
    Blue = [0] * N
    Red = [0] * N # 흰색, 파란색, 빨간색을 세어 줄 빈 리스트 생성

    for i in range(N-2):
        cnt = 0
        for j in range(len(flag[i])):
            if flag[i][j] != 'W':
                cnt += 1
        White[i] = cnt

    for i in range(1, N-1):
        cnt = 0
        for j in range(len(flag[i])):
            if flag[i][j] != 'B':
                cnt += 1
        Blue[i] = cnt

    for i in range(2, N):
        cnt = 0
        for j in range(len(flag[i])):
            if flag[i][j] != 'R':
                cnt += 1
        Red[i] = cnt

    # print(White)
    # print(Blue)
    # print(Red)
    result = []

    for w in range(1, N - 1):
        for b in range(1, N - 1):
            for r in range(1, N - 1):
                if w + b + r == N:
                    result.append((w, b, r))
                elif w + b + r > N:
                    break

    ans = 0
    min_num = 2501
    for i, j, k in result:
        ans += sum(White[:i])
        ans += sum(Blue[i:i + j])
        ans += sum(Red[i + j:i + j + k])
        if ans < min_num:
            min_num = ans
        ans = 0

    print('#{} {}'.format(tc, min_num))
