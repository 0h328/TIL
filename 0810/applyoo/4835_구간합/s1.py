import sys
sys.stdin = open('input.txt')

def section(arr, N, M):
    DP = [arr[0]] + [0] * (N-1)
    result = [0] * (N-M+1)

    for i in range(1, N):
        DP[i] = DP[i-1] + arr[i]

    result[0] = DP[M-1]
    for i in range(1, N-M+1):
        result[i] = DP[M+i-1] - DP[i-1]

    return max(result) - min(result)

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print('#{} {}'.format(i + 1, section(arr, N, M)))