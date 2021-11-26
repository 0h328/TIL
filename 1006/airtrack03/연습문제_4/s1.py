"""
연습 문제4. 트리 순회
 문제4-1) 주어진 입력 정보를 활용하여 트리를 그려보고 각 순회 별로 어떤 순서로 노드를 방문하는지 작성하시오.

 문제4-2) 다음 이진 트리 표현에 대하여 전위/중위/후회 순회하여 정점의 번호를 출력하시오
     첫 줄에는 트리의 정점의 총 수 V가 주어진다. 그 다음 줄에는 V-1개 간선이 나열된다.
     간선은 그것을 이루는 두 정점으로 표기된다. 간선은 항상 '부모 자식' 순서로 표기된다.
     아래 예에서 두 번째 줄 처음 1과 2는 정점 1과 2를 잇는 간선을 의미하며 1이 부모, 2가 자식을 의미한다.
     간선은 부모 정점 번호가 작은 것부터 나열되고, 부모 정점이 동일하다면 자식 정점 번호가 작은 것부터 나열된다.
"""


# 전위 순회 (V -> L -> R)
def pre_order(node):
    print(node, end=' ')
    if left[node]:
        pre_order(left[node])
    if right[node]:
        pre_order(right[node])


# 중위 순회 (L -> V -> R)
def in_order(node):
    if left[node]:
        pre_order(left[node])
    print(node, end=' ')
    if right[node]:
        pre_order(right[node])


# 후위 순회 (L -> R -> V)
def post_order(node):
    if left[node]:
        pre_order(left[node])
    if right[node]:
        pre_order(right[node])
    print(node, end=' ')


import sys

sys.stdin = open('input.txt')

N = int(input())
data = list(map(int, input().split()))
left = [0] * (N+1)
right = [0] * (N+1)

for i in range(len(data)//2):
    p, c = data[2*i], data[2*i+1]
    if not left[p]:
        left[p] = c
    else:
        right[p] = c


print('전위 순회 : ', end='')
pre_order(1)
print()

print('중위 순회 : ', end='')
in_order(1)
print()

print('후위 순회 : ', end='')
post_order(1)
print()