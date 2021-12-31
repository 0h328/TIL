import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def find(arr):
    k = 1   # 맨 처음에 픽했으니 사탕 개수 1개

    for i in range(N):
        cnt = 1 # 연속될때마다 사탕 개수 +1 하기 위한 cnt
        for j in range(1, N):
            if arr[i][j] == arr[i][j-1]:    # 인접한 곳이 동일한 색일때 (열끼리)
                cnt += 1                    # 사탕 개수 +1
            else:                           # 그렇지 않으면
                cnt = 1                     # 사탕 개수 1개 유지

            if k < cnt:
                k = cnt

        cnt = 1
        for j in range(1, N):
            if arr[j][i] == arr[j-1][i]:    # 인접한 곳이 동일한 색일때 (행끼리)
                cnt += 1                    # 사탕 개수 +1
            else:                           # 그렇지 않으면
                cnt = 1                     # 사탕 개수 1개 유지

            if k < cnt:
                k = cnt

    return k

N = int(input())
arr = [list(input()) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(N-1):
        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j] # 열끼리 인접한 곳 교환

        tmp = find(arr) # 교환됐을떄, 가장 긴 연속 부분(사탕의 최대 개수) 찾기

        if ans < tmp:
            ans = tmp

        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j] # 원상복구

for i in range(N-1):
    for j in range(N):
        arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j] # 행기리 인접한 곳 교환

        tmp = find(arr) # 교환됐을떄, 가장 긴 연속 부분(사탕의 최대 개수) 찾기

        if ans < tmp:
            ans = tmp

        arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j] # 원상복구

print(ans)