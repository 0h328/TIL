import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())

calc = {0: lambda x: x+1, 1: lambda x: x-1, 2: lambda x: x*2, 3: lambda x: x-10}


def bfs(start):
    global ans
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        cur = q.popleft()

        for d in range(4):
            nxt = calc[d](cur)

            if 0 < nxt <= M+10:
                if visited[nxt] == -1:
                    visited[nxt] = visited[cur] + 1
                    q.append(nxt)

                    if nxt == M:
                        ans = visited[nxt]
                        return


# b_calc = {0: lambda x: x-1, 1: lambda x: x+1, 2: lambda x: x//2 if not x&1 else 0, 3: lambda x: x+10}


for tc in range(1, T+1):
    N, M = map(int, input().split())

    visited = [-1] * (M+11)
    ans = 0
    bfs(N)

    # result = [-1] * (10*M)
    # result[N] = 0
    #
    # for i in range(N, 0, -1):
    #     for j in (1, 3):
    #         nxt_idx = f_calc[j](i)
    #
    #         if result[i] != -1:
    #             if result[nxt_idx] != -1:
    #                 result[nxt_idx] = min(result[i] + 1, result[nxt_idx])
    #             else:
    #                 result[nxt_idx] = result[i] + 1
    #
    # if N < M:
    #     for i in range(N, M+1):
    #         for j in range(4):
    #             nxt_idx = f_calc[j](i)
    #
    #             if nxt_idx < 1 or nxt_idx > 1000001:
    #                 continue
    #
    #             if result[i] != -1:
    #                 if result[nxt_idx] != -1:
    #                     result[nxt_idx] = min(result[i] + 1, result[nxt_idx])
    #                 else:
    #                     result[nxt_idx] = result[i] + 1


    print('#{} {}'.format(tc, ans))
