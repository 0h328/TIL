import sys
sys.stdin = open('input2.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # print(N)

    my_list = [list(map(int, input().split())) for _ in range(N)]
    print(my_list)

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    i = 0
    j = 0

    result = 0

    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            for k in range(4):
                nr = dr[k] + i
                nc = dc[k] + j
                if 0 <= nr < N and 0 <= nc < N:
                    result += abs(my_list[nr][nc]-my_list[i][j])

    print(result)