import sys
sys.stdin = open('input.txt')


def in_order(node):
    if node:
        in_order(arr[node - 1][2])  # 왼쪽
        print('{}'.format(arr[node - 1][1]), end='')  # 노드
        in_order(arr[node - 1][3])

for idx in range(10):
    N = int(input())
    arr = [[0] * 4 for _ in range(N)]
    for i in range(N):
        r = input().split()
        for j in range(len(r)):
            if r[j].isdecimal():
                arr[i][j] = int(r[j])
            else:
                arr[i][j] = r[j]


    print('#{}'.format(idx + 1), end = ' ')
    in_order(1)
    print()
