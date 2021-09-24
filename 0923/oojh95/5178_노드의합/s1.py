import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split()) # 정보를 받아옴
    tree = [0 for _ in range(N + 2)] # 트리를 만드는데 완전이진트리에 자식노드가 다 차있는 것으로 가정해서 만듬
    for _ in range(M):
        leap, num = map(int, input().split())   # 가장 아래 leap노드에 값들을 입력해줌
        tree[leap] = num
    i = N // 2  # leap레벨의 상위 레벨에서 각각 합계를 구하기 위해 다음과 같은 노드에서부터 정보를 채워 나가며 상위 레벨로 올라갈 것
    while i > 0:    #최종적으로 level = 0인 상태까지 가기 위한 조건
        tree[i] = tree[i*2] + tree[i*2+1]  # 하위 2개의 노드 정보로부터 합산하여 계산
        i -= 1 # 더 작은 번호의 노드에서 결과를 구하기 위해 하나씩 빼나감.

    print('#{} {}'.format(tc, tree[L]))
