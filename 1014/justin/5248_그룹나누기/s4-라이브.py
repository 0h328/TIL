import sys

sys.stdin = open('input_5248.txt', 'r')


# def BFS(st):
#     Q = [st]
#     team[st] = 1
#     while Q:
#         p = Q.pop(0)
#         for i in range(1, N+1):
#             if not team[i] and adj_arr[p][i]:
#                 team[i] = 1
#                 Q.append(i)
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())# N: 사람 수, M: 신청서 수
#
#     edges = list(map(int, input().split()))
#
#     adj_arr = [[0]*(N+1) for _ in range(N+1)] #인접 행렬을 준비하자.
#
#     # for i in range(0,len(edges),2):
#
#     for i in range(M):
#         a = edges[i*2]
#         b = edges[i*2+1]
#
#         adj_arr[a][b] = adj_arr[b][a] = 1
#
#     ans = 0
#
#     team = [0] * (N+1)
#
#     for i in range(1, N+1):
#         if not team[i]:
#             ans+=1
#             BFS(i)
#
#     print("#{} {}".format(tc, ans))

############################################
def find_set(x):
    while p[x] != x:
        x = p[x]
    return x


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N: 사람 수, M: 신청서 수

    edges = list(map(int, input().split()))

    p = [i for i in range(N + 1)]  # 대표 원소를 각자 자신으로 초기화
    # p = list(range(N+1))

    for i in range(M):
        a = edges[2*i]
        b = edges[2*i+1]

        p[find_set(b)] = find_set(a)

    ans = 0

    for i in range(1, N+1):
        if p[i] == i:
            ans += 1

    print("#{} {}".format(tc, ans))