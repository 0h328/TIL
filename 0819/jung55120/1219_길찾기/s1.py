def dfs(v):
    stack = [v]

    while stack:
        v = stack.pop()
        if v == 99:
            return 1

        if not visited[v]:
            visited[v] = 1
            # print('방문 정점: {}, 방문 체크: {}'.format(v, visited))

            for w in range(0, 100):
                if G[v][w] == 1 and not visited[w]:
                    stack.append(w)

    return 0



import sys
sys.stdin = open('input.txt')

for tc in range(10):
    # tc, E(dge)
    tc, E = map(int, input().split())

    # 간선 정보 초기화
    temp = list(map(int, input().split()))
    # print(temp)

    # Graph 초기화
    G = [[0 for _ in range(100)] for _ in range(100)]
    # print(G)
    # print(DataFrame(G))

    # 인접 행렬
    for i in range(E):
        G[temp[i*2]][temp[i*2+1]] = 1

    # print(G)

    # 방문 표시 초기화
    visited = [0 for _ in range(100)]
    # print(visited)
    # dfs 탐색 시작
    print('#{} {}'.format(tc, dfs(0)))



# import sys
# sys.stdin = open('input.txt')
#
# def step(idx, cnt, max):
#     if path1[idx] == 99 or path2[idx] == 99:
#         return 99
#     elif path1[idx] == True and cnt <= max:
#         cnt_temp = cnt + 1
#         return step(path1[idx], cnt_temp, max)
#     elif path2[idx] == True and cnt <= max:
#         cnt_temp = cnt + 1
#         return step(path2[idx], cnt_temp, max)
#
# for _ in range(10):
#     tc, E = map(int, input().split())
#     temp = list(map(int, input().split()))
#
#     path1 = [0] * 100
#     path2 = [0] * 100
#
#
#     for i in range(E):
#         if not path1[temp[i * 2]]:
#             path1[temp[2 * i]] = temp[2 * i + 1]
#         else:
#             path2[temp[2 * i]] = temp[2 * i + 1]
#     # print(path1)
#     # print(path2)
#     cnt = 0
#     result = 0
#     if step(0, cnt, E*E) == 99:
#         result = 1
#     else:
#         result = 0
#     print('#{} {}'.format(tc,result))