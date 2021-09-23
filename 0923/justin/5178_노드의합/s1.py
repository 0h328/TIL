import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) # N: 전체 노드 수 / M: 단말(리프/잎) 노드의 수 / L: 출력 할 노드 번호
    tree = [0] * (N+1)                  # 루트 노드를 기준으로 왼쪽 자식(v*2) / 오른쪽 자식(v*2+1) -> 배열의 인덱스 활용
    for _ in range(M):                        # 리프 노드의 값 세팅
        num, val = map(int, input().split())  # num: 리프 노드의 번호 / val: 리프노드 num에 들어있는 숫자
        tree[num] = val                       # num번 노드의 val 세팅

    # 리프 노드의 값을 토대로 노드의 합 세팅
    # 전체 노드 수 - 단말 노드 수 (리프 노드를 제외한 자식 노드에 접근하기 위함) ~ 1번까지(0번은 제외)
    for i in range(N-M, 0, -1):
        # 완전 이진 트리에서 마지막 레벨이 아닌 경우 반드시 '왼쪽 자식'은 있다.
        # 마지막 레벨에서는 '오른쪽 자식'만 있는 경우는 없다. (왼쪽만 존재)
        # tree[i] = tree[i*2] + tree[i*2+1]
        tree[i] = tree[i*2]  # 부모에 왼쪽 자식의 값을 넣고
        if i*2+1 <= N:              # 오른쪽 자식의 범위를 체크(부모 * 2 -> 왼쪽 / 부모 * 2 + 1 -> 오른쪽)
            tree[i] += tree[i*2+1]  # 왼쪽 리프 노드의 값 + 오른쪽 리프 노드의 값

    ans = tree[L]  # L번 노드에 저장된 값
    print('#{} {}'.format(tc, ans))
