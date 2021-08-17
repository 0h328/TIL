import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(T):
    N, M = map(int, input().split())
    words = [list(map(str, input())) for _ in range(N)]
    col_words = list(zip(*words))

    for n in range(N):
        for k in range(N):
            tmp1 = []
            tmp2 = []
            if k + M <= N:
                tmp1 = words[n][k:k + M]
                if list(tmp1) == list(reversed(tmp1)):
                    print('#{} {}'.format(num + 1, "".join(tmp1)))

                tmp2 = col_words[n][k:k + M]
                if list(tmp2) == list(reversed(tmp2)):
                    print('#{} {}'.format(num + 1, "".join(tmp2)))
