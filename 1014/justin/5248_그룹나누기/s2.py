# 상호배타집합 활용
def make_set(x):
    p[x] = x

# 재귀구조
def find_set(x):
    """
    여기서 인덱스와 부모가 같은 경우까지 계속 찾아간다.
    5번 정점 f의 경우 부모가 자신의 인덱스와 다르기 때문에 -> 4번으로 가게 되고 -> 4번도 부모와 다르기 때문에 다시 2번으로 가게 된다.
    2번은 부모와 자신이 같기 때문에 대표값으로 자기 자신을 반환
       인덱스   0  1  2  3  4  5
       정점    a  b  c  d  e  f
       부모    0  1  2  2  2  4
    """
    if p[x] != x: # 대표자가 다른 경우
        # p[x] = find_set(x) 이렇게 작성하지 않도록 유의
        # x가 아닌 x의 대표값을 구해야 하기 때문에 재귀적으로 호출하며 p[x] == x를 찾아야 함
        p[x] = find_set(p[x])
    return p[x]                           # 대표자가 같은 경우 그 값을 반환

# 반복 구조
# def find_set(x):
#     while p[x] != x:
#         x = p[x]
#     return x

def union(x, y):
    p[find_set(y)] = find_set(x)          # rank가 없기 때문에 x, y의 순서는 크게 중요하지 않음

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = list(map(int, input().split()))

    # p = list(range(V+1))
    p = [0] * (V+1)                       # V번까지 활용하기 위해 V+1로 초기화
    for i in range(V+1):
        make_set(i)

    """
    print(p)
    1. 처음 초기화된 상태
      0 1 2 3 4 5 6 7
    p 0 1 2 3 4 5 6 7
    """

    for i in range(E):
        A = edge[i*2]; B = edge[i*2+1]
        union(A, B)

    """
    print(p)
    2. union 이후
      0 1 2 3 4 5 6 7 
    p 0 1 2 2 7 4 4 7
    """

    for i in range(1, V+1):  # V+1 -> V번까지 돌며
        find_set(i)          # 바꿀 수 있는 값은 모두 변경(대표값)
    """
    print(p)
    3. 대표값 갱신
      0 1 2 3 4 5 6 7 
    p 0 1 2 2 7 7 7 7
    """

    # 대표원소를 찾는 버전 - 반복문
    # cnt = 0
    # for i in range(1, V+1): # 대표원소수 == 그룹 수
    #     if p[i] == i:
    #         cnt += 1

    # 중복 요소를 제외하고 만들어진 그룹 확인
    # 인덱스 연산 때문에 0부터 시작했으니 그 값을 제외
    ans = len(set(p))-1
    print('#{} {}'.format(tc, ans))