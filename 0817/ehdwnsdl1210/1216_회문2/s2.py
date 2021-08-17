import sys
sys.stdin = open('input.txt')

T = int(input())

def find_pal():
    # 모든 행에 대해서
    for row in range(N):
        for s in range(0, N - M + 1):
            e = s + M - 1
            for i in range(M // 2):
                if arr[row][s + i] != arr[row][e - i]:
                    break

            else:   # 회문인 경우
                ret = ''
                for i in range(s, e + 1):
                    ret += arr[row][i]
                return ret

    # 모든 열에 대해서
    for col in range(N):
        for s in range(0, N - M + 1):
            e = s + M - 1
            for i in range(M // 2):
                if arr[s + i][col] != arr[e - i][col]:
                    break

            else:   # 회문인 경우
                ret = ''
                for i in range(s, e + 1):
                    ret += arr[i][col]
                return ret

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    print('#{} {}'.format(tc, find_pal()))