import sys
sys.stdin = open('input.txt')

def dfs(n):
    global cnt
    if tree[n]:                                                   # tree의 n 노드에 값이 존재하는가
        for node in tree[n]:
            cnt += 1                                              # 존재하는 경우 cnt + 1
            dfs(node)
    return cnt

for tc in range(int(input())):
    e, n = map(int, input().split())
    node_list = list(map(int, input().split()))
    cnt = 1                                                       # 첫번째 받는 N도 추가해주기 위해서 1로 설정
    tree = [[] for i in range(e+2)]                               # 노드의 개수가 1~e+1까지
    for i in range(e):
        parent, child = node_list[i*2], node_list[i*2+1]          # 부모, child로 받아줌
        tree[parent].append(child)
    print(tree)
    print('#{}'.format(tc + 1), end = ' ')
    # print(tree)
    print(dfs(n))
