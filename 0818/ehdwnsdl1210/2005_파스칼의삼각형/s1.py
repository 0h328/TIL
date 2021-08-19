# 문제 설계
# 문제 풀이
# 디버깅 (정답 유무)

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    result = [[0] for _ in range(N)]

    for i in range(N):
        result[i][0] = 1

        if i > 0:
            result[i].append(1)

            if i > 1:
                for j in range(1, i):
                    result[i].insert(j, result[i-1][j-1] + result[i-1][j])

    print('#{}'.format(tc))
    for i in result:
        print(*i)