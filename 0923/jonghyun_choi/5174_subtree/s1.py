import sys
sys.stdin = open('input.txt')

def order(node):
    global ans
    if node != 0:
        ans += 1
        order(tree[node][0])  # 왼쪽
        order(tree[node][1])

T = int(input())

for case in range(T):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(max(temp) + 1)]
    ans = 0
    for idx in range(E):
        parent, child = temp[idx * 2], temp[idx * 2 + 1]
        if not tree[parent][0]:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
        tree[parent][2] = parent

    order(N)
    print('#{} {}'.format(case + 1, ans))