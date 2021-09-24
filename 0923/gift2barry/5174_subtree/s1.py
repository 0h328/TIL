import sys
sys.stdin = open('input.txt')

# 디버깅 20분
# 풀이시간 40분
# thought process: 10분
# 순회 작업을 N 노드부터 시작
# 중위순회로 모든 자식 노드에 접근
# 접근 할 때마다 카운트

def in_order(n):
    global cnt
    if n:
        cnt += 1
        in_order(l[n])
        # cnt += 1
        in_order(r[n])
        # cnt += 1
    return


for tc in range(1, int(input())+1):
    E, N = map(int, input().split())
    tree = list(map(int, input().split()))
    l = [0] * (E+2)
    r = [0] * (E+2)
    cnt = 0

    for i in range(E):
        p, c = tree[i*2], tree[i*2+1]
        if l[p] == 0:
            l[p] = c
        else:
            r[p] = c

    in_order(N)
    print('#{} {}'.format(tc, cnt))















# def in_order(n, i):
#     global cnt
#     if tree[i+1]:
#         cnt += 1
#         for j in range(tree.index(tree[i+1]), E*2-1):
#             if tree[j] == tree[i+1] and j % 2 == 0:
#                 in_order(tree[i+1], j)
#     return
#
#
# for tc in range(1, int(input())+1):
#
#     E, N = map(int, input().split())
#     tree = list(map(int, input().split()))
#     cnt = 0
#
#     for i in range(E*2-1):
#         if tree[i] == N and i % 2 == 0:
#             in_order(N, i)
#             break
#
#     print('#{} {}'.format(tc, cnt))