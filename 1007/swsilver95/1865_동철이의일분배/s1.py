import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def dfs(idx, p):
    global answer
    if idx == N:
        if answer < p:
            answer = p
            return

    if answer >= p:
        return

    for i in range(N):
        if not check[i]:
            check[i] = True
            dfs(idx + 1, p * (prob[idx][i] / 100))
            check[i] = False


for tc in range(1, T + 1):
    N = int(input())
    prob = [list(map(int, input().split())) for _ in range(N)]
    check = [False] * N
    answer = 0
    dfs(0, 1)

    print('#{} {:.6f}'.format(tc, answer * 100))

