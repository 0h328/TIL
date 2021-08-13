import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for i in range(N)]

    result = []
    point = []
    for r in range(M):
        for c in range(M):
            point.append((r,c))

    for j in range(N):   # 0
        for k in range(N): # 0, 1, 2, 3
            fly_catch = []
            if 0 <= j <= N - M and 0 <= k <= N - M:
                for l in range(len(point)): # 0, 1, 2
                    nj = j + point[l][0]
                    nk = k + point[l][1]
                    fly_catch.append(arr[nj][nk])
                result.append(sum(fly_catch))
    print('#{0} {1}'.format(tc, max(result)))