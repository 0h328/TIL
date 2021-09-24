import sys
sys.stdin = open('input.txt')

def value_at(node):

    if not G[node]:     # 0이면
        G[node] = value_at(node*2)  # 자식에서 하나 추가

        if node*2 + 1 <= N:         # 오른쪽도 있으면
            G[node] += value_at(node*2+1)   # 추가

    return G[node]


for tc in range(int(input())):
    N, M, L = map(int, input().split())
    G = [0 for _ in range(N+1)]

    for _ in range(M):
        node, val = map(int, input().split())
        G[node] = val

    # print(G)
    ans = value_at(L)
    # print(G)

    # ans = 0
    print('#{0} {1}'.format(tc+1, ans))
    # break
