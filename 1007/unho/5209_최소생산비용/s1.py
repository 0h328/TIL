import sys
sys.stdin = open('input.txt')


def permu(factory, ans):        # permutation
    global answer

    if factory >= N:            # 최솟값 판별 후 저장
        if answer > ans:
            answer = ans
        return
    elif ans > answer:          # Pruning
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            permu(factory+1, ans + table[i][factory])
            visited[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    answer = 1e10

    permu(0, 0)

    print('#{} {}'.format(tc, answer))