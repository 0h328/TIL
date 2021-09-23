import sys
sys.stdin = open('input.txt')


def fill(node):
    global tree, cnt
    if node < N+1:
        fill(node*2) # 왼쪽부터 돌고
        tree[node] = cnt # 채우고
        cnt += 1
        fill(node*2 + 1) # 오른쪽 돌고


T = int(input())
for t in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    cnt = 1

    fill(1)
    print('#{} {} {}'.format(t, tree[1], tree[N//2]))