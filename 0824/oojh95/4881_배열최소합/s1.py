import sys
sys.stdin = open('input.txt')
def dfs(r,c):
    global result
    if result > min_val:
        return
          # 다음 반복문을 위해 원상복구.



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    min_val = 9 * N
    result = 0
    dfs(0,0)


