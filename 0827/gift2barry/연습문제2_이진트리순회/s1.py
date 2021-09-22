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
2) 트리는 1차원 배열 / 2차원 배열 모두 표현이 가능. 일단은 1차원으로 접근해보자.
"""

# thought process:
# left 리스트와 right 리스트 생성 후, 해당 위치에 숫자들을 넣는다
# 해당 위치 원소값이 0 이면 없다는 뜻.
# recursion 로직 활용해서 왼쪽 이동 가능하면 계속 왼쪽 이동 하다가
# 오른쪽도 확인해라.
# 전위, 중위, 후위에 따라서 print() 적는 위치만 바꿔줘라.
# recursion으로 방문하는 코드 자체는 똑같다. 그냥 왼쪽 먼저 방문하고 오른쪽 방문이다.

# 문제:
# 왜 중위 순회와 후위 순회는 제대로 된 답이 안 나올까..
# recursive 코딩 로직에 이상은 없어보인다만..

# 해결:
# recusion 대상 함수들의 함수명이 불일치하여 수정.

# 전위 순회 (V -> L -> R)
def pre_order(n):
    if n:
        print(n, end=' ')    # 1, 2, 4
        pre_order(left[n])
        pre_order(right[n])

# 중위 순회 (L -> V -> R)
def in_order(n):
    if n:
        in_order(left[n])
        print(n, end=' ')
        in_order(right[n])

# 후위 순회 (L -> R -> V)
def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(n, end=' ')

import sys
sys.stdin = open('input.txt')

V = int(input())                        # 13
E = V - 1                               # 간선 개수
nums = list(map(int, input().split()))  # 노드 위치들
print(nums)
left = [0] * (V+1)      # 좌측 트리 값으로 저장
right = [0] * (V+1)     # 우측 트리 값으로 저장

for i in range(E):
    p, c = nums[i*2], nums[i*2+1]       # 짝수 일때 parent 숫자, 홀수 일때 child 숫자

    if left[p] == 0:                    # parent 노드에 좌측에 자식이 없으면,
        left[p] = c                     # 좌측에 자식 값 할당
    else:                               # parent 좌측 노드에 자식 있으면
        right[p] = c                   # 우측에 자식 값 할당


pre_order(1)
# 1 -> 2 -> 4 -> 7 -> 12 -> 3 -> 5 -> 8 -> 9 -> 6 -> 10 -> 11 -> 13
print()


in_order(1)
# 12 -> 7 -> 4 -> 2 -> 1 -> 8 -> 5 -> 9 -> 3 -> 10 -> 6 -> 13 -> 11
print()


post_order(1)
# 12 -> 7 -> 4 -> 2 -> 8 -> 9 -> 5 -> 10 -> 13 -> 11 -> 6 -> 3 -> 1
print()