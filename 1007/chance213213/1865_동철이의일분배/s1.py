import sys
sys.stdin = open('input.txt')

def check(j):
    global total, visited, result
    if j == N:
        return
    if total > result:
        result = total

    for i in range(N):
        if not visited[i][j]:#값이 없을 때? 맞지?
            visited[i][j] = 1
            if percents[i][j] != 0:
                total *= percents[i][j]
            check(j+1)
            if percents[i][j] != 0:
                total /= percents[i][j]
            visited[i][j] = 0

    return total



#i번 직원이 j번 일을 하면 성공할 확률은 Pi,j?
#주어진 일이 모두 성공할 확률의 최댓값을 구하는 프로그램

#입력 안에 확률이 들어있구나

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #N명이 있는 거임

    percents = [list(map(int, input().split())) for _ in range(N)]

    #이제 최대 확률을 구해야 함, i, j 하나씩 다 관찰하면 되려나?
    total = 1
    visited = [[0] * N for _ in range(N)]
    result = -1
    check(0)