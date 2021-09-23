# 리프 노드(leaf node) : 자식이 없는 노드

# def output(L):
#     if tree[L][0] != 0 or tree[L][1] != 0:          # 자식이 하나라도 있다면
#         if tree[L][0] != 0:                         # 왼쪽이 있으면
#             tree[L][3] += tree[tree[L][0]][3]       # 왼쪽 값 더함
#         if tree[L][1] != 0:                         # 오른쪽이 있으면
#             tree[L][3] += tree[tree[L][1]][3]       # 오른 값 더함
#
#     return tree[L][3]

def pre_order(L):
    if L != 0:
        tree[L//2][3] += tree[L][3] # 부모에게 내 값을 주고
        pre_order(tree[L][0])  # 왼쪽
        pre_order(tree[L][1])  # 오른쪽

    return tree[L][3]

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    tree = [[0 for _ in range(4)] for _ in range(N+1)]  # 끝에 value 칸 삽입! (range(4))

    for i in range(1, (N // 2) + 1):
        tree[i][0] = i * 2
        tree[i][2] = i // 2
        tree[2 * i][2] = i

        if N % 2 == 0:                          # N 이 짝수인 경우, 마지막 경우를 해주면 안됨
            if i != (N // 2):                   # 마지막이 아니면 다 해주고, 마지막인 경우 제외
                tree[i][1] = i * 2 + 1
                tree[2 * i + 1][2] = i
        elif N % 2 == 1:                        # N 이 홀수인 경우, 다 가능
            tree[i][1] = i * 2 + 1
            tree[2 * i + 1][2] = i

    for _ in range(M):
        node, value = map(int, input().split())
        tree[node][3] = value

    print('#{} {}'.format(tc, pre_order(L)))