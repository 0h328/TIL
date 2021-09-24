def dfs(v):
    if v > N:        # N이 마지막 수 -> v가 이보다 클 수 없음 -> 이런 경우 0을 리턴
        return 0
                     # 후위 순회 -> 값을 누적하는 작업을 왼쪽과 오른쪽을 모두 다녀온 뒤에 진행
    l = dfs(v*2)     # 왼쪽으로 이동
    r = dfs(v*2+1)   # 오른쪽으로 이동
    tree[v] += l + r # 값을 누적 (비어있는 공간은 0을 return)
    return tree[v]   # 누적한 값을 return

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())       # N: 전체 노드 수 / M: 단말(리프/잎) 노드의 수 / L: 출력 할 노드 번호
    tree = [0] * (N+1)                        # 루트 노드를 기준으로 왼쪽 자식(v*2) / 오른쪽 자식(v*2+1)
    for _ in range(M):
        num, val = map(int, input().split())  # num: 리프 노드의 번호 / val: 리프노드 num에 들어있는 숫자
        tree[num] = val                       # num번 노드의 값(val)

    dfs(1)
    ans = tree[L]
    print('#{} {}'.format(tc, ans))