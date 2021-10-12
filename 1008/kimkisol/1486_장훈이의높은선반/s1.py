import sys

# 357ms
sys.stdin = open('input.txt')


# a |= a << num 방식으로도 풀 수 있음!

def dfs(idx, h):
    global min_h

    if min_h < h:
        return
    if idx == N:
        if B <= h < min_h:  # POINT) 기준 높이보다 같거나 커야 함
            min_h = h
        return

    for i in range(2):  # POINT) 0: 포함, 1: 미포함
        if i:
            dfs(idx + 1, h)
        else:
            dfs(idx + 1, h + H[idx])


T = int(input())

for t in range(1, T + 1):
    N, B = map(int, input().split())  # N: 점원 수, B: 기준 높이
    H = list(map(int, input().split()))  # H: 점원 키
    min_h = N * 10000  # 점원 수 * 최대 키

    dfs(0, 0)
    print('#{} {}'.format(t, min_h - B))
