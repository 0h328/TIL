import sys
sys.stdin = open('input.txt')

def pre_order(N):
    global cnt
    if N != 0:
        cnt += 1
        pre_order(tree[N][0])
        pre_order(tree[N][1])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    cnt = 0
    tree = [[0 for _ in range(3)] for _ in range(E+2)]

    for i in range(E):
        parent, child = temp[i*2], temp[i*2+1]
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
        tree[child][2] = parent

    pre_order(N)

    print('#{} {}'.format(tc, cnt))