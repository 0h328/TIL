import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree_arr = [0] * (N+1)

    for _ in range(M):                              # 1차원 배열, 해당 노드 번호 인덱스에 값 추가
        node, value = map(int, input().split())
        tree_arr[node] = value

    for idx in range(N-M, L-1, -1):                 # 가장 맨뒤 첫 부모노드부터 시작,
        tree_arr[idx] = tree_arr[idx*2]
        if idx*2 + 1 <= N:                          # 오른쪽 노드도 있으면 값 추가
            tree_arr[idx] += tree_arr[idx*2 + 1]

    print('#{} {}'.format(tc, tree_arr[L]))