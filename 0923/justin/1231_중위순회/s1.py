def in_order(node):
    if node != 0:
        in_order(left_child[node])
        print(alphabet[node], end='')
        in_order(right_child[node])

import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    N = int(input())            # 총 정점의 수
    left_child = [0] * (N+1)    # 인덱스 번호를 활용하기 위히야 정점수+1로 지정
    right_child = [0] * (N+1)
    alphabet = [0] * (N+1)
    for i in range(N):          # 정점(노드)의 개수 만큼 반복하며 트리 정보 구성
        temp = input().split()  # 정점 번호, 정점 번호에 해당하는 알파벳, 왼쪽, 오른쪽 자식
        addr = int(temp[0])     # 정점 번호 (LVR중 V에 해당)
        char = temp[1]          # 알파벳
        alphabet[addr] = char   # 정점 번호에 알파벳 기록

        if addr*2 <= N:                           # 왼쪽 자식만 있는 경우 (마지막 노드를 넘지 않으면)
            left_child[addr] = int(temp[2])       # 왼쪽 자식 추가 (완전 이진 트리는 오른쪽 자식만 존재할 수는 없음)
            if addr*2+1 <= N:                     # 오른쪽 자식도 있는 경우(완전 이진 트리)
                right_child[addr] = int(temp[3])  # 오른쪽 자식 추가
    print('#{}'.format(tc), end=' ')
    in_order(1)
    print()