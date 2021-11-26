'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

# tree와 graph의 차이점
# tree는 싸이클이 없다.
def pre_order(n):
    global cnt
    if n:
        cnt += 1 # print(n, end=' ')
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
par = [0] * (V+1)

# 각각의 노드를 번호에 따라 입력
for i in range(E):
    p, c = edge[2*i], edge[2*i+1]

    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p      # 조상을 찾는데 사용


# c = 6               # 조상찾기
# while par[c]:       # 부모가 유효하면
#     print(par[c])
#     c = par[c]

# 부모가 없으면 루트임.
# root = 1
# while par[root]:    # 루트로 추정한 정점이 부모가 있으면
#     root += 1


cnt = 0
pre_order(3)    # 시작점 1
print(cnt)      # 3을 루트로하는 서브트리의 정점 개수
print(cnt-1)    # 3의 자손의 개수
