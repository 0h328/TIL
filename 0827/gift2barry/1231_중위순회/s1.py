# 소요시간: 약 5시간
# 4번째 try
# thought process: 20분
# 완전 이진트리는 dfs 탐색 순서라는걸 바탕으로
# tree 리스트에 tree 순서대로 단어들만 입력받고
# 각 노드의 숫자 * 2 는 좌측 자식 노드이고,
# 각 노드의 숫자 * 2 + 1 는 우측 자식 노드이다
# 위 노트를 바탕으로 recursion 활용하여
# 좌측자식 노드 => 부모노드 => 우측자식노드 순으로
# ans 단어들 ans 에 저장

#
import sys
sys.stdin = open('input.txt')


def in_order(v):
    global ans
    if v * 2 <= N:
        in_order(v * 2)
    ans += tree[v]
    if v * 2 + 1 <= N:
        in_order(v * 2 + 1)


for tc in range(1, 10+1):

    N = int(input())
    tree = [0] * (N + 1)  # tree
    ans = ''
    for i in range(N):
        var = input().split()
        tree[int(var[0])] = var[1]
    in_order(1)
    print('#{} {}'.format(tc, ans))