import sys
sys.stdin = open("input.txt")

T = 10

def in_order(root):
    if tree[root][1]:
        in_order(tree[root][1])
    print(tree[root][0], end='')
    if tree[root][2]:
        in_order(tree[root][2])

for tc in range(1, T+1):
    N = int(input())

    tree = [[0 for _ in range(3)] for _ in range(N+1)]

    for _ in range(N):
        left, right = 0, 0 # 초기화 안하면 기존 left, right 값이 남아있어서 재귀 문제 발생
        data = input().split()
        cur = int(data[0])
        char = data[1]
        if len(data) > 2:
            left = int(data[2])
        if len(data) > 3:
            right = int(data[3])

        tree[cur][0] = char
        tree[cur][1] = left
        tree[cur][2] = right

    root = 1
    print('#{}'.format(tc), end=' ')
    in_order(root)
    print()
