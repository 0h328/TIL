import sys
sys.stdin = open('input.txt')

def cnt(node, cnt2):
    if tree[node][0] != 0:
        cnt2 = cnt(tree[node][0], cnt2 + 1)

    if tree[node][1] != 0:
        cnt2 = cnt(tree[node][1], cnt2 + 1)
    return cnt2

tc = int(input())
for t in range(1, tc + 1):
    result = 0
    E, N = map(int, input().split())
    E_list = list(map(int, input().split()))
    tree = [[0, 0] for _ in range(E + 2)]
    for e in range(E):
        if tree[E_list[2 * e]][0] == 0:
            tree[E_list[2 * e]][0] = E_list[2 * e + 1]
        else:
            tree[E_list[2 * e]][1] = E_list[2 * e + 1]
    print(tree)
    result = cnt(N, 1)

    print("#{} {}".format(t, result))