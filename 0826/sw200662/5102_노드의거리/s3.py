import sys

sys.stdin = open('input.txt')

T = int(input())


def find(x):
    global ans
    que = []
    que.append(x)
    visit[x] = 1

    while que:
        z = que.pop(0)
        for k in range(1, V + 1):
            if list_node[z][k] and visit[k] == 0:
                visit[k] = 1
                que.append(k)
                distance[k] = distance[z] + 1
                if k == G:
                    ans = distance[k]
                    return
    return


for i in range(T):
    V, E = map(int, input().split())
    list_node = [[0] * (V + 1) for _ in range(V + 1)]
    visit = [0] * (V + 1)
    distance = [0] * (V + 1)
    for _ in range(E):
        A, B = map(int, input().split())
        list_node[A][B] = 1
        list_node[B][A] = 1
    ans = 0
    S, G = map(int, input().split())
    find(S)
    print('#{} {}'.format(i + 1, ans))
