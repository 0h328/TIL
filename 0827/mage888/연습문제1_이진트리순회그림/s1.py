'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

# tree와 graph의 차이점
# tree는 싸이클이 없다.
def pre_order(n):
    if n:
        print(n, end=' ')
        pre_order(left[n])
        pre_order(right[n])

# 노드 개수

import sys
sys.stdin = open('input.txt')

V = int(input())

# 간선 정보
edge = list(map(int, input().split()))

# V개의 정점이 있는 트리의 간선 수
E = V-1

# 부모를 인덱스로 자식 번호 저장
left = [0] * (V+1)  # 부모의 왼쪽 자식 저장 (인덱스 번호 맞추기)
right = [0] * (V+1) # 부모의 오른쪽 자식 저장 (인덱스 번호 맞추기)

# 각각의 노드를 번호에 따라 입력
for i in range(E):
    p, c = edge[2*i], edge[2*i+1]

    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

pre_order(1)