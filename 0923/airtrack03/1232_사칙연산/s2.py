import sys
sys.stdin = open('input.txt')

T = 10

def calc(v):
    if len(tree[v]) == 2:
        return tree[v][1]
    else:
        L = calc(tree[v][2])
        R = calc(tree[v][3])

        if tree[v][1] == '+':
            return L + R
        elif tree[v][1] == '-':
            return L - R
        elif tree[v][1] == '*':
            return L * R
        elif tree[v][1] == '/':
            return L / R


for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)

    for i in range(1, N+1):
        temp = input().split()

        tree[int(temp[0])] = temp

        if len(temp) == 4:
            tree[int(temp[0])][2] = int(tree[int(temp[0])][2])
            tree[int(temp[0])][3] = int(tree[int(temp[0])][3])
        else:
            tree[int(temp[0])][1] = int(tree[int(temp[0])][1])

    print('{} {}'.format(tc, int(calc(1))))