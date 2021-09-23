def post_order(node):
    global cal
    if node:
        post_order(int(tree[node][1]))
        post_order(int(tree[node][2]))
        cal.append(tree[node][0])


import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    N = int(input())
    tree = [['0' for _ in range(3)] for _ in range(N + 1)]
    cal = []
    stack = []

    for i in range(1, N+1):
        info = list(input().split())
        if len(info) >= 2:
            tree[i][0] = info[1]
        if len(info) == 4:
            tree[i][1] = info[2]
            tree[i][2] = info[3]

    post_order(1)

    for char in cal:
        if char == '+':
            x = stack.pop()
            y = stack.pop()
            stack.append(x + y)
        elif char == '*':
            x = stack.pop()
            y = stack.pop()
            stack.append(x * y)
        elif char == '-':
            x = stack.pop()
            y = stack.pop()
            stack.append(y - x)
        elif char == '/':
            x = stack.pop()
            y = stack.pop()
            stack.append(y / x)
        else:
            stack.append(int(char))

    ans = int(stack.pop())
    print('#{} {}'.format(test_case, ans))


