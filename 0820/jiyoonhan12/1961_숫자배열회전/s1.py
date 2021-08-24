import sys
sys.stdin = open('input.txt')

# 스스로 풀기
T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    for i in range(N):
        for j in range(N):
            arr90[i][j] = arr[N-j-1][i]
