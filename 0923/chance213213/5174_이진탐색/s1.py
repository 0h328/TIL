import sys
sys.stdin = open('input.txt')

def in_order(v):
    global cnt
    if v <= N:
        in_order(v*2)
        tree[v] = cnt
        cnt += 1
        in_order(v*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    cnt = 1
    in_order(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))