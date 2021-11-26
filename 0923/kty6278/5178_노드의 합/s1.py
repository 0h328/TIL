import sys
sys.stdin = open('input.txt')


for tc in range(int(input())):
    n, m, l = list(map(int, input().split()))
    tree = [0 for _ in range(n+1)]
    for i in range(m):
        node, num = map(int, input().split())
        tree[node] = num                               # 각노드에 리프노드 값만 추가
    # print(tree)
    for i in range(n, 1, -1):                          # 노드 2부터 n까지 노드 1은 2,3에서 해결, 맨뒤에서부터 2까지
        tree[i // 2] += tree[i]                        # 값을 누적시키면서 이전의 //2 노드에 더해주는 방식
    print(tree)
    print('#{} {}'.format(tc+1, tree[l]))