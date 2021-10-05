'''
사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때의 최소 배터리 사용량은?
각 구역을 이동할 때의 배터리 사용량은 표로 제공,
1번은 사무실을, 2번부터 N번은 관리구역 번호이다.
두 구역 사이도 갈 때와 올 때의 경사나 통행로가 다를 수 있으므로 배터리 소비량은 다를 수 있음
N이 3인 경우 가능한 경로는 1-2-3-1, 1-3-2-1이며,
각각의 배터리 소비량은 다음과 같이 계산할 수 있다.
e[1][2]+e[2][3]+e[3][1] = 18+55+18 = 91
e[1][3]+e[3][2]+e[2][1] = 34+7+48 = 89
이 경우 최소 소비량은 89가 된다.
'''


def DFS_SUM(n):
    global min_num
    global sum_num
    global section_set


    if len(section_set) == 0:
        sum_num += cc[n][0]

        if min_num > sum_num:
            min_num = sum_num
            return

    for i in section_set:
        if sum_num > min_num:
            return
        sum_num += cc[n][i]
        section_set.remove(i)


        for j in section_set:
            if sum_num > min_num:
                return
            sum_num += cc[i][j]


            section_set.remove(j)
            DFS_SUM(j)
            sum_num -= cc[j][i]
            section_set = {i for i in range(1, N)}


import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cc = [list(map(int, input().split())) for _ in range(N)]
    # print(cc)
    min_num = 987654321
    sum_num = 0

    section_set = {i for i in range(1, N)}
    DFS_SUM(0)

    print('#{} {}'.format(tc, min_num))
# 1 89
# 2 96
# 3 139