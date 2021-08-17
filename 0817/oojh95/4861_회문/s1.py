import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]
    result = ''

    for i in range(N):
        for j in range(N - M + 1):
            for k in range(M // 2):
                if words[i][j + k] != words[i][j + M - k - 1]:
                    break
            else:
                result = ''.join(words[i][j:j + M])
                print('#{} {}'.format(test_case, result))

            for k in range(M // 2):
                if words[j + k][i] != words[j + M - k - 1][i]:
                    break
            else:
                result = ''
                for m in range(M):
                    result += words[j + m][i]
                print('#{} {}'.format(test_case, result))

