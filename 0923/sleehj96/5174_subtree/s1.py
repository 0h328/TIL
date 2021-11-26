import sys
sys.stdin = open('input.txt')


def childs_count(node):
    global cnt
    cnt += 1    # 지나칠 때마다 +1

    for w in G[node]:       # 자식 순회
        childs_count(w)     # 재귀


for tc in range(int(input())):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    G = [[] for _ in range(E+1+1)]  # E+1+1 = node개수+1

    for i in range(E):
        p, c = edges[2*i], edges[2*i+1]
        G[p].append(c)

    cnt = 0
    childs_count(N)     # N을 루트로 자손을 세자
    print('#{0} {1}'.format(tc+1, cnt))
    # break
