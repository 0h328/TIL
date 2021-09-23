import sys
sys.stdin = open('input.txt')


def post_order(node):
    global cal
    if 0 < node < N+1:
        post_order(left[node])
        post_order(right[node])
        cal.append(tree[node])

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        return a / b


for t in range(1, 11):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    tree = [0] * (N+1)

    for _ in range(N):
        idx, val, *child = map(str, input().split())
        if child:
            left[int(idx)] = int(child[0])
            tree[int(idx)] = val
            try:
                right[int(idx)] = int(child[1])
            except:
                pass
        else:
            tree[int(idx)] = int(val)

    cal = []
    post_order(1)

    oper = ['+', '-', '*', '/']
    stack = []

    for char in cal:
        if char not in oper:
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            temp = calculate(a, b, char)
            stack.append(temp)

    ans = int(stack.pop())

    print('#{} {}'.format(t, ans))