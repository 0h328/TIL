import sys
sys.stdin = open('input.txt')

def pre_order(node):
    global cnt
    if node != 0:
        cnt += 1
        pre_order(tree[node][0])
        pre_order(tree[node][1])

T = int(input())

for t in range(T):
    E, N = list(map(int, input().split()))
    temp = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(E + 2)]

    cnt = 0
    for i in range(E):
        parent, child = temp[i * 2], temp[i * 2 + 1]
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
        tree[child][2] = parent

    pre_order(N)
    print('#{} '.format(t+1), end='')
    print(cnt)
