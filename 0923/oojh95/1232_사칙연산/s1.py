import sys
sys.stdin = open('input.txt')

def post_order(node):
    if node != 0:
        post_order(tree[node][0])           # 왼쪽
        post_order(tree[node][1])           # 오른쪽
        if tree[node][3] in cal:
            stack.append(cal[tree[node][3]](stack.pop(), stack.pop()))
        else:
            stack.append(tree[node][3])

for tc in range(1, 11):
    N = int(input())
    tree = [[0 for _ in range(4)] for _ in range(N+1)]
    stack = []
    cal = {
        '+': lambda x, y: y + x,
        '-': lambda x, y: y - x,
        '*': lambda x, y: y * x,
        '/': lambda x, y: y // x,
    }
    for i in range(1, N+1):
        arr = list(input().split())
        if len(arr) == 2:
            tree[i][3] = int(arr[1])
        else:
            tree[i][0] = int(arr[2])
            tree[i][1] = int(arr[3])
            tree[i][2] = int(arr[0])
            tree[i][3] = arr[1]
    post_order(1)
    result = stack.pop()
    print('#{} {}'.format(tc, result))
