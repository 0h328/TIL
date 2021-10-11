import sys
sys.stdin = open('input.txt')


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def dfs(i, j, c, letters):
    global numbers

    if c > 6:
        numbers.add(letters)
        return

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(ni, nj, c+1, letters + arr[ni][nj])



T = int(input())
for t in range(1, T+1):
    arr = [list(map(str, input().split())) for _ in range(4)]
    numbers = set()

    # 시작점 결정
    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, arr[i][j])
    # dfs 돌기
    print('#{} {}'.format(t, len(numbers)))