import sys
sys.stdin = open('input.txt')


def calc(v):
    if len(tree[v])==2:
        return tree[v][1]
    else:
        L = calc(tree[v][2])
        R = calc(tree[v][3])

        if tree[v][1] == '+': return L+R
        elif tree[v][1] == '-': return L-R
        elif tree[v][1] == '*': return L*R
        elif tree[v][1] == '/': return L/R

    # if n <= N:                    # 자식이 있는 정점이면
    #     in_order(n*2)   # n의 왼쪽 자식으로 이동
    #     print(tree[n], end='')
    #     in_order(n*2+1)  # n의 오른쪽 자식으로 이동

for tc in range(1, 11):
    N = int(input())
    tree = [0]*(N+1)
    for i in range(N):
        tmp = input().split()
        tree[i+1] = tmp
        if len(tmp) == 4:   #자식이 두개임
            tree[i+1][2] = int(tree[i+1][2])
            tree[i+1][3] = int(tree[i+1][3])
        else:
            tree[i+1][1] = int(tree[i+1][1])
    print('#{} {}'.format(tc, int(calc(1))))
