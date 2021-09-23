import sys
sys.stdin = open('input.txt')

def order(n):
    global cnt
    if n <= N:
        order(2*n)
        tree[n] = cnt
        cnt += 1
        order(2*n + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    cnt = 1

    order(1)

    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))