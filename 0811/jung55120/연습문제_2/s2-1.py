import sys
sys.stdin = open('input2.txt')

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    my_list = [list(map(int, input().split())) for _ in range(N)]
    # print(my_list)
    result = 0

    for i in range(N):
        for j in range(N): # my_list[0][0]
            for k in range(len(di)):
                if 0 <= i+di[k] < N and 0 <= j+dj[k] < N:
                    result += abs(my_list[i+di[k]][j+dj[k]] - my_list[i][j])

    print('#{} {}'.format(tc, result))