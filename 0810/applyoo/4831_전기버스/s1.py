import sys
sys.stdin = open('input.txt')

def charging(arr, K, N, M):
    state = result = 0

    arr.sort()
    for i in range(M-1):
        if arr[i+1] - arr[i] > K:
            return 0

    while state <= N:
        for i in range(K, 0, -1):
            if (state+i) in arr:
                state += i
                result += 1
        print(state)

    return result

T = int(input())

for i in range(T):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print('#{} {}'.format(i + 1, charging(arr, K, N, M)))