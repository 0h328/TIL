import sys
sys.stdin = open('input.txt')

def calculate(i):
    if len(tree[i]) == 2:
        return int(tree[i][1])
    a = calculate(int(tree[i][2]))
    b = calculate(int(tree[i][3]))
    if tree[i][1] == '+':
        return a + b
    elif tree[i][1] == '-':
        return a - b
    elif tree[i][1] == '*':
        return a * b
    else:#/
        return a // b
    return calculate()



for idx in range(1, 11):
    n = int(input())
    tree = [[]] + [input().split() for _ in range(n)]

    print('#{} {}'.format(idx, calculate(1)))