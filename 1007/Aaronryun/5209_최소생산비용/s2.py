import sys
from pandas import DataFrame
sys.stdin = open('input.txt')


# def dfs(idx, rec): # 000~111
#     if rec == (1 << N) - 1: # rec가 결국  N이 3인경우에는 111이 되어야 끝난다
#         return 0
#     if temp[rec]: # 만약 값이 존재한다면 방문한 곳 이건 그냥 반환
#         return temp[rec]
#
#     p = 1e9
#     for i in range(N): # 3인 경우 0,1,2 의 조합을 구해야 한다. 결과적으로 rec는 111이 되지만 선택되는 순서가 중요
#         if data[idx][i] and not (rec & (1 << i)): # 값이 0 인 경우는 해줄 필요가 없음, 한번도 선택하지 않은것
#             p = min(p, data[idx][i] + dfs(idx + 1, rec | (1 << i))) # 다 더한 것중의 최소 data[0][0]+data[0][1]+data[0][2]+0
#
#     temp[rec] = p #
#     return p

def Dfs(idx,rec):
    temp = [0] * (1 << N)  # 더 빠른 연산을 위한
    temp[0]=0
    for mask in range(1<<N):
        x = bin(mask).count('1')
        for j in range(N):
            if not mask & (1<<j):
                temp[mask|(1<<j)] = max(temp[mask|(1<<j)],temp[mask]+data[x][j])
    return temp

for test in range(1, 1 + int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]


    answer = Dfs(0, 0)
    print('#{} {}'.format(test, answer))
