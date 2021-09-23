# 문제 푼 시간
# 풀이법:
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

"""
첫 줄에는 트리의 정점의 총 수 V가 주어진다. 그 다음 줄에는 V-1개 간선이 나열된다.
간선은 그것을 이루는 두 정점으로 표기된다. 간선은 항상 '부모 -> 자식' 순서로 표기된다.
아래 예에서 두 번째 줄 처음 1과 2는 정점 1과 2를 잇는 간선을 의미하며 1이 부모, 2가 자식을 의미한다.
간선은 부모 정점 번호가 작은 것부터 나열되고, 부모 정점이 동일하다면 자식 정점 번호가 작은 것부터 나열된다.

다음 이진 트리 표현에 대하여 전위/중위/후회 순회하여 정점의 번호를 출력하시오.
13 -> 정점의 개수
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

참고)
1) Tree에서는 정점의 개수만 알려줘도 간선 정보를 알 수 있음 (정정미 V개 일 때 간선은 V-1개)
2) 트리는 1차원 배열 / 2차원 배열 모두 표현이 가능하지만 이 문제는 2차원으로 접근 해보자
"""

# 전위 순회 (V -> L -> R)
def pre_order(node):

    print(node, end=" ")
    if tr[node][0]:
        pre_order(tr[node][0])

    if tr[node][1]:
        pre_order(tr[node][1])


# 중위 순회 (L -> V -> R)
def in_order(node):
    if tr[node][0]:
        in_order(tr[node][0])
    print(node, end=" ")

    if tr[node][1]:
        in_order(tr[node][1])


# 후위 순회 (L -> R -> V)
def post_order(node):
    if tr[node][0]:
        post_order(tr[node][0])
    if tr[node][1]:
        post_order(tr[node][1])

    print(node, end=" ")


n = int(input())
lst = list(map(int, input().split()))
tr = {i: [0, 0, 0] for i in range(1, max(lst) + 1)}

for i in range(0, len(lst), 2):
    p, s = lst[i], lst[i + 1]
    tr[s][2] = p
    if tr[p][0]:
        tr[p][1] = s
    else:
        tr[p][0] = s

print("전위 순회 : ", end="")
pre_order(1)
print()

print("중위 순회 : ", end="")
in_order(1)
print()

print("후위 순회 : ", end="")
post_order(1)
print()