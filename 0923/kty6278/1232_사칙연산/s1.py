import sys
sys.stdin = open('input.txt')

# def solve(tree, root):
# 대실패........ 인덱스 맞춰서 데이터 입력 받아오는게 힘들다

for tc in range(10):
    n = int(input())
    tree = [[] for i in range(n+1)]
    for _ in range(n):
        node = list(map(str, input().split()))
        tree[int(node[0])] = node[1:]
    # print(tree) # [[], ['-', '2', '3'], ['-', '4', '5'], ['10'], ['88'], ['65']]
    for i in range(len(tree)):
        if len(tree[i]) == 3:
            value = tree[i][0]
            left = tree[i][1]
            right = tree[i][2]
        elif len(tree[i]) == 1:
            value = tree[i][0]
            left, right = 0, 0