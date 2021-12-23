import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def horizon(r, c):

    if 0 <= r < N and 0 <= c < M:   # 범위내
        if arr[r][c] == '-':        # -면
            arr[r][c] = 'x'         # x로 바꾸고
            horizon(r, c+1)         # 오른쪽 탐색 / 왼쪽은 이미 x로 바꾸고 왔으니 탐색할 필요없음
            return True
        return False

def vertical(r, c):

    if 0 <= r < N and 0 <= c < M:   # 범위내
        if arr[r][c] == '|':        # |면
            arr[r][c] = 'x'         # x로 바꾸고
            vertical(r+1, c)        # 아래 탐색 / 위쪽은 이미 x로 바꾸고 왔으니 탐색할 필요없음
            return True
        return False


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == '-':
            horizon(i, j)       # 되돌아올때, 연결된 -를 모두 탐색하고 돌아옴. 방문한 곳 다 x로 바꾸기 때문
            cnt += 1
        elif arr[i][j] == '|':  # else가 아니라 elif로 한 이유는 방문하면 'x'로 바꾸기 때문에 else를 하면 'x'도 찾는다.
            vertical(i, j)      # 되돌아올때, 연결된 |를 모두 탐색하고 돌아옴. 방문한 곳 다 x로 바꾸기 때문
            cnt += 1

print(cnt)

# 풀이2
# N, M = map(int, input().split())
# floor = [list(input()) for _ in range(N)]
# ans = 0
# for i in range(N):
#     cng = '.'
#     for j in range(M):
#         if floor[i][j] == '-':
#             if floor[i][j] != cng:
#                 ans += 1
#         cng = floor[i][j]
# for i in range(M):
#     cng = '.'
#     for j in range(N):
#         if floor[j][i] == '|':
#             if floor[j][i] != cng:
#                 ans += 1
#         cng = floor[j][i]
# print(ans)