import sys
sys.stdin = open('input.txt')

def post_order(v):
    if v >= N:
        return

    if tree[v][2] > 0:  # 2번 인덱스가 왼쪽
        post_order(tree[v][2])
    if tree[v][3] > 0:  # 3번 인덱스가 오른쪽이기 때문
        post_order(tree[v][3])


    # 연산자에 따라 계산을 해야하는데.....

for t in range(10):
    N = int(input())
    tree = [[0] * 4 for _ in range(N + 1)]

    for n in range(N):
        root = list(input().split())
        if root[1].isdigit():       # 숫자인지
            tree[int(root[0])][1] = int(root[1])
        else:                       # 연산자인지
            tree[int(root[0])][1] = root[1]
            tree[int(root[0])][2] = int(root[2])
            tree[int(root[0])][3] = int(root[3])

    post_order(1)

    print("#{} {}".format(t+1, tree[1][1]))