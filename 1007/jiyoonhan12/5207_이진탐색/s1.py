import sys
sys.stdin = open('input.txt')


def binary_search(arr, n, l, r):
    global ans, dir
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == n:           # 중간에 중단되지 않고 target 찾았으면 ans += 1 하고 종료
            ans += 1
            return
        elif arr[mid] < n:
            l = mid + 1
            if dir == 1:            # 이전에도 오른쪽 탐색했으면 종료
                return
            dir = 1
        else:
            r = mid - 1
            if dir == -1:           # 이전에도 왼쪽 탐색했으면 종료
                return
            dir = -1
    return                          # 다 돌았는데 못찾았으면 종료

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    ans = 0

    for num in B:
        dir = 0                             # 이전에 어떤 쪽 탐색했는지 저장할 변수
        binary_search(A, num, 0, N-1)

    print('#{} {}'.format(t, ans))