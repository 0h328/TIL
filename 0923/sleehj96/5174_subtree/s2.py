import sys
sys.stdin = open('input.txt')

def childs_count(node):
    global cnt

    if node:
        cnt += 1    # 0이 아니면 세자
        childs_count(G[node][0])
        childs_count(G[node][1])


for tc in range(int(input())):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    G = [[0, 0] for _ in range(E+1+1)]  # E+1+1 = node개수+1

    for i in range(E):
        p, c = edges[2*i], edges[2*i+1]
        if not G[p][0]:
            G[p][0] = c
        else:
            G[p][1] = c

    cnt = 0
    childs_count(N)     # N을 루트로 자손을 세자
    print('#{0} {1}'.format(tc+1, cnt))
    # break
