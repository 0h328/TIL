import sys
sys.stdin = open('input.txt')
from collections import deque

operators = [1, -1, 2, -10]
def BFS(s, e, cnt):
    global min_cnt
    Q = deque()
    Q.append((s, cnt))

    while Q:
        s, cnt = Q.popleft()
        if s == e:
            if min_cnt > cnt:
                min_cnt = cnt
                return
        for i in operators:
            if i == 1:
                if 0 < s + 1 <= M + 10:
                    Q.append((s + 1, cnt + 1))
            elif i == -1:
                if 0 < s - 1 <= M + 10:
                    Q.append((s - 1, cnt + 1))
            elif i == 2:
                if 0 < s * 2 <= M + 10:
                    Q.append((s * 2, cnt + 1))
            else:
                if 0 < s - 10 <= M + 10:
                    Q.append((s - 10, cnt + 1))

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())        # N : 자연수, M : 목표 자연수 / 최소 몇번해서 N -> M
    min_cnt = 987654321
    BFS(N, M, 0)
    print('#{} {}'.format(tc, min_cnt))







'''
import sys
sys.stdin = open('input.txt')

operators = [1, -1, 2, -10]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())        # N : 자연수, M : 목표 자연수 / 최소 몇번해서 N -> M

    dp = [0] * 1000001
    dp[0] = 1
    # print(dp)

    while dp[M] == 0:
        for i in range(1000000, -1, -1):
            for j in range(4):
                if dp[i] > 0:
                    if j == 0:
                        if i + 1 > 0:
                            if dp[i + 1] == 0:
                                dp[i + 1] = dp[i] + 1
                            else:
                                dp[i + 1] = min(dp[i + 1], dp[i] + 1)

                    elif j == 1:
                        if i - 1 > 0:
                            if dp[i - 1] == 0:
                                dp[i - 1] = dp[i] - 1
                            else:
                                dp[i - 1] = min(dp[i - 1], dp[i] - 1)

                    elif j == 2:
                        if i * 2 > 0:
                            if dp[i * 2] == 0:
                                dp[i * 2] = dp[i] * 2
                            else:
                                dp[i * 2] = min(dp[i * 2], dp[i] * 2)

                    else:
                        if i - 10 > 0:
                            if dp[i - 10] == 0:
                                dp[i - 10] = dp[i] - 10
                            else:
                                dp[i - 10] = min(dp[i - 10], dp[i] - 10)

    print('#{} {}'.format(tc, dp[M] - 1))
'''

#1 3
#2 4
#3 8