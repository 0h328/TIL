import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(N)]

ans = 0
tmp = min(N, M)

for i in range(N):
    for j in range(M):
        for k in range(tmp):
            if i+k < N and j+k < M: # 정사각형 범위 안에서만
                if arr[i][j] == arr[i+k][j] == arr[i][j+k] == arr[i+k][j+k]: # 각 꼭지점의 숫자가 같은 경우
                    ans = max(ans, (k+1)*(k+1)) # 정사각형의 넓이가 큰 경우를 계속 갱신해준다.

print(ans)
