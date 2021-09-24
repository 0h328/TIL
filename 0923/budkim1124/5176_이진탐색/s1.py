import sys
sys.stdin = open('input.txt')


def in_order(n):
    global cnt
    if n <= N:
        in_order(n*2)
        tree[n] = cnt
        cnt += 1
        in_order(n*2 + 1)

T = int(input())

for t in range(T):
    N = int(input())
    cnt = 1
    tree = [0] * (N + 1)

    in_order(1)
    print('#{} {} {}'.format(t+1, tree[1], tree[N//2]))