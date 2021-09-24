import sys
sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M): # 값을 트리에 저장
        node, value = map(int, input().split())
        tree[node] = value

    for i in range(N, 0, -1):
        if not i % 2: # 짝수일때만 옆이랑 더함
            if i+1 <= N and tree[i+1]: # 옆에 노드 하나 더 있다면(홀수)
                tree[i//2] = tree[i] + tree[i+1]
            else:
                tree[i//2] = tree[i]

    print('#{} {}'.format(t, tree[L]))