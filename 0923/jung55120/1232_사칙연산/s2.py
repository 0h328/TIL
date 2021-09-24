import sys
sys.stdin = open('input.txt')

def calculus(node):
    if node != 0:
        if tree[node][0] == '+':
            return calculus(tree[node][1]) + calculus(tree[node][2])
        elif tree[node][0] == '-':
            return calculus(tree[node][1]) - calculus(tree[node][2])
        elif tree[node][0] == '*':
            return calculus(tree[node][1]) * calculus(tree[node][2])
        elif tree[node][0] == '/':
            return calculus(tree[node][1]) / calculus(tree[node][2])
        else:
            return int(tree[node][0])


for tc in range(1, 11):
    N = int(input())
    tree = [[0 for _ in range(3)] for _ in range(N+1)]
    for i in range(1, N+1):
        temp = list(input().split())
        # print(temp)
        if len(temp) == 4:
            tree[i][0] = temp[1]
            tree[i][1] = int(temp[2])
            tree[i][2] = int(temp[3])
        else:
            tree[i][0] = int(temp[1])


    print('#{0} {1}'.format(tc, int(calculus(1))))


