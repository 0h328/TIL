import sys
sys.stdin = open('input.txt')

# 완전 이진 트리

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())  # 노드의 개수 N, 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    node_value = [0] * (N + 1)

    for i in range(M):
        temp = list(map(int, input().split()))
        node_value[temp[0]] = temp[1]

    if N % 2 == 0:
        node_value.append(0)

    for j in range(N//2, 0, -1):
        node_value[j] = node_value[2*j] + node_value[2*j+1]

    print('#{} {}'.format(tc, node_value[L]))




