import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())                         # 노드 개수
    temp = list(map(int, input().split()))   # 노드값 정보
    heap = [0] * (N+1)                       # 1부터 시작
    heap_size = 0                            # 마지막을 가리키는 (stack의 top과 같은) + 힙의 크기를 나타내는 변수
    for val in temp:                         # 입력으로 받은 값을 하나씩 가져와서
        heap_size += 1                       # stack의 top처럼 사이즈 증가(heap_size는 heap의 전체 크기)
        heap[heap_size] = val                # 완전 이진 트리의 모양을 유지 시키기 위해서 일단 가장 마지막에 추가

        child = heap_size                    # 자식과 부모의 값을 저장해놓고(heap_size 자체가 변화하면 안되니 복사)
        parent = heap_size // 2              # 부모 인덱스 맞춰놓고

        """
        종료 조건
        1. 부모가 루트 (0)
            - 부모가 0이 되기전까지 진행
            - 루트가 1이기 때문에 1//2 ->0
        2. 부모 > 자식 (최소힙)
            - 부모가 더 크면? 최소힙의 조건에 맞지 않는다.
        """
        while parent and heap[parent] > heap[child]:                # 새로 추가된 값이 부모 보다 작은지 / 큰지 여부 확인 -> 최소힙 규칙
            heap[parent], heap[child] = heap[child], heap[parent]   # 우선 자리 변경 -> 변경한 자리에서 부모와 자식의 위치가 바뀜
            child = parent                                          # 부모는 자식이 되고
            parent = child // 2                                     # 자식은 부모가 된다.

    ans = 0
    v = N // 2                  # 마지막 인덱스? N (1부터 N까지) & 마지막 노드의 부모 노드 ? N // 2 -> 계속 부모를 찾아가자!
    while v:                    # v가 0이 되기전까지 -> 루트가 되기전까지
        ans += heap[v]          # 방문하면서 v(노드) 위치에 있는 값을 누적
        v //= 2                 # 다시 V의 //2 -> 부모
    print('#{} {}'.format(tc, ans))