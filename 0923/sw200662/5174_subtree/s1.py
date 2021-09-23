import sys

sys.stdin = open('input.txt')

def find_node(node):
    global cnt

    if node != 0:
        cnt += 1
        find_node(tree[node][0])
        find_node(tree[node][1])



T = int(input())

for i in range(T):
    E, N = input().split()
    E, N = int(E), int(N)

    tree = [[0, 0, 0]] + [[0, 0, 0] for _ in range(E + 1)]

    temp = list(map(int, input().split()))
    for k in range(E):
        if tree[temp[k * 2]][0] == 0:
            tree[temp[k * 2]][0] = temp[k * 2 + 1]
            tree[temp[k * 2 + 1]][2] = temp[k*2]
        else:
            tree[temp[k * 2]][1] = temp[k * 2 + 1]
            tree[temp[k * 2 + 1]][2] = temp[k * 2]
    cnt = 0
    find_node(N)
    print('#{} {}'.format(i+1,cnt))