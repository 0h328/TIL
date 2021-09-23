import sys
sys.stdin = open('input.txt')


# thought process: 3분
# 후외순회 활용
# 왼쪽 오른쪽 자식의 합을 부모 노드에 부여
# 이 방식으로 끝까지 순회 후,
# 루트 노드 원소 값 반환


for tc in range(1, int(input())+1):
    # 노드개수, 리프노드개수, 값을출력할노드번호
    N, M, L = map(int, input().split())
    tree = [0] * (N+2)

    for _ in range(M):
        n, e = map(int, input().split())
        tree[n] = e

    i = N//2
    while i > 0:
        tree[i] = tree[i*2] + tree[i*2+1]
        i -= 1

    print('#{} {}'.format(tc, tree[L]))