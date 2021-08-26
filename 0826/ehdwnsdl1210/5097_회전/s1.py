import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(arr)

    for _ in range(M):
        arr.append(arr.pop(0))

    print('#{} {}'.format(tc, arr[0]))
    # [M % N]