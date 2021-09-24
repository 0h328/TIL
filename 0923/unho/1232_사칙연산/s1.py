import sys
sys.stdin = open('input.txt')


def calc(op, num1, num2):
    if op == '+': return num1 + num2
    elif op == '-': return num1 - num2
    elif op == '*': return num1 * num2
    elif op == '/': return num1 / num2

def post_order(node):
    if str(tree[node][1]).isdigit():
        return int(tree[node][1])

    return calc(tree[node][1], post_order(int(tree[node][2])), post_order(int(tree[node][3])))

for tc in range(1, 11):
    N = int(input())

    tree = [[]]

    for _ in range(N):
        tree.append(input().split())

    answer = post_order(1)

    print('#{} {}'.format(tc, int(answer)))