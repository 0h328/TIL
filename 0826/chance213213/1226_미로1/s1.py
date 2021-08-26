import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    ans = 0

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                # start_i, start_j = i, j
                start = (i, j)
                break

    visited = [start]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while visited:
        i, j = visited.pop()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if -1 < ni < 16 and -1 < nj < 16:
                if arr[ni][nj] == 0:
                    visited.append((ni, nj))
                    #여기 가볼게, 가보고 막히면 이길은 다시 가도 의미 없음. 가장 최근 갈림길로 back하고 다른 길로 가라
                    arr[ni][nj] = 1

                elif arr[ni][nj] == 3:
                    ans = 1
                    visited.clear()
                    break

    print('#{} {}'.format(tc, ans))


# def checking(i, j):
#     global find
#     # ni == end[0] and nj == end[1]:
#     if find == 1:
#         return 1
#
#     if arr[i][j] == 3:
#         find = 1
#         return 1
#
#     visited[i][j] = 1
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#
#     for k in range(4):
#         ni = i + di[k]
#         nj = j + dj[k]
#
#         if -1 < ni < 16 and -1 < nj < 16 and arr[ni][nj] == 0 and (ni, nj) and visited[ni][nj] == 0:
#             # queue.append((ni, nj))
#             # visited[ni][nj] = 1
#             checking(ni, nj)
#         # else:
#         #     ni -= di[k]
#         #     nj -= dj[k]
#         #

    # for i in range(15, -1, -1):
    #     for j in range(15, -1, -1):
    #         if arr[i][j] == 3:
    #             # end_i, end_j = i, j
    #             end = (i, j)
    #             break


    # visited = [[0] * 16 for _ in range(16)]
    # visited = arr[::]
    # queue = []
    # visited = arr[::]
    # m_i = start[0]
    # m_j = start[1]
    #
    # find = 0
    #
    # print(checking(m_i, m_j))



