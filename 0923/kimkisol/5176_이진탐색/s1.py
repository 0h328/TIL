import sys

sys.stdin = open('input.txt')


def in_order(t):
    global n
    if t <= N:  # N보다 작은 범위 내에서
        in_order(t * 2)  # 왼쪽 자식
        tree[t] = n  # 1~N까지 순차 대입
        n += 1
        in_order(t * 2 + 1)  # 오른쪽 자식


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    n = 1

    in_order(1)

    print('#{} {} {}'.format(t, tree[1], tree[N // 2]))
