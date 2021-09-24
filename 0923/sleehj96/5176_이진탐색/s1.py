import sys
sys.stdin = open('input.txt')


def in_order(node):
    global num

    if node*2+1 <= N:       # leaf node 2개
        in_order(node*2)
        G[node] = num
        num += 1
        in_order(node*2+1)

    elif node*2 <= N:       # leaf node 왼쪽 하나
        in_order(node*2)
        G[node] = num
        num += 1

    elif node <= N:         # 내가 leaf node
        G[node] = num
        num += 1


for tc in range(int(input())):
    N = int(input())
    G = [0 for _ in range(N+1)]

    num = 1
    in_order(1)
    print('#{0} {1} {2}'.format(tc+1, G[1], G[N//2]))
    # break
