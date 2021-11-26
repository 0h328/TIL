import sys
sys.stdin = open('input.txt')

# for _ in range(10):
#     N = int(input())
#     L = [list(map(int, input().split())) for _ in range(100)]
#     idx = [[-1, 0], [0, -1], [1, 0], [0, 1]] # 상좌하우(참고용)
#     s = []
#     for i in range(100):
#         for j in range(100):
#             if L[i][j] == 2:
#                 s = [i, j]
#
#     while s[0] > 0:
#             if L[s[0] - 1][s[1]] == 1:
#                 s[0] -= 1
#             elif L[s[0]][s[1] - 1] == 1:
#                 s[1] -= 1
#             elif L[s[0]][s[1] + 1] == 1:
#                 s[1] += 1
#
#     print('#{} {}'.format(N, s[1]))

def search(start): # 도착지에서 위로 올라가는 함수
    i = 99 # 행
    j = start # 열
    while i > 0: # 맨 윗줄 도착 전까지 올라감
        i -= 1 # 위로 1칸 (양 옆에 0이 없는것)
        if j > 0 and ladder[i][j-1] == 1:         # 왼쪽 1? 벽만나면?
            while j > 0 and ladder[i][j-1] == 1:  # 0을 만날 때 까지 이동
                j -= 1
        elif j < 99 and ladder[i][j+1] == 1:       # 오른쪽 1? 벽만나면?
            while j < 99 and ladder[i][j+1] == 1:  # 99을 만날 때 까지 이동
                j += 1
    return j # 0번 행에 도착했을 때의 열(출발지) 반환

T = 10
for tc in range(1, T+1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착지 검색
    goal = 0
    for i in range(100):
        if ladder[99][i] == 2:
            goal = i
    ans = search(goal)

    print('#{} {}'.format(tc, ans))