import sys
sys.stdin = open('input.txt')

# 2를 찾아서
# 역으로 가는데
# 갈래길 나오면 무조건 위 → 좌 / 좌 → 우
# 최종 X 위치는? (인덱스로) / [0][result]까지

for _ in range(10):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(100)]

    idx = [[-1, 0], [0, -1], [1, 0], [0, 1]] # 상좌하우(참고용)

    s = []
    for i in range(100):
        for j in range(100):
            if L[i][j] == 2:
                s = [i, j]

    while s[0] > 0:
        if -1 < s[0] < 100 and -1 < s[1] < 100:
            if s[1] == 0:
                s[1] = 0

            elif L[s[0]][s[1] - 1] == 0 and L[s[0] - 1][s[1]] == 1:
                s[0] -= 1

            elif L[s[0]][s[1] - 1] == 1:
                s[1] -= 1

    print('#{} {}'.format(N, s[1]))