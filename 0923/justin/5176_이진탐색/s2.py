def solve(node):
    global idx
    if node <= N:               # N은 마지막 노드 번호
        solve(node*2)           # 왼쪽 서브트리 방문
        tree[node] = idx        # 중위 순회로 현재 노드값 저장
        idx += 1
        solve(node*2+1)         # 오른쪽 서브트리 방문

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    idx = 1
    tree = [0 for i in range(N+1)]      # 노드 번호 == 인덱스
    solve(1)                            # 1번 노드부터 시작
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))