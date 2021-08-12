import sys

sys.stdin = open('input.txt')

T = int(input())

for test in range(T):
    N, M = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(len(data) - (M - 1)):
        for j in range(len(data[i]) - (M - 1)):
            msum = 0
            for h in range(M):
                for k in range(M):
                    msum += data[j + k][i + h]
            if msum > result:
                result = msum

    print('#{} {}'.format(test + 1, result))
