import sys

sys.stdin = open('input_5207.txt', 'r')


def binary_search_while(key):
    l = 0  # 시작
    r = N - 1  # 끝

    d = -1  # 왼쪽구간을 탐색했다 0, 오른쪽구간 탐색 1
    while l <= r:
        mid = (l + r) // 2
        # 찾았다면
        if key == A[mid]:
            return 1
        elif key < A[mid]:
            if d == 0: return 0
            r = mid - 1
            d = 0
        else:
            if d == 1: return 0
            l = mid + 1
            d = 1
    return 0

def binary_search_recusion(l, r, d, key):
    if l > r : return 0
    else:
        mid = (l+r)//2

        if key == A[mid]: return 1
        elif key <A[mid]:
            # if d != 0:
            #     return binary_search_recusion(l, mid-1, 0, key)
            if d == 0 : return 0
            else: return binary_search_recusion(l, mid-1, 0, key)
        else:
            if d != 1:
                return binary_search_recusion(mid+1, r, 1, key)

    return 0


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # A와 B의 원소수
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()

    ans = 0

    for i in B:
        # ans += binary_search_while(i)
        ans += binary_search_recusion(0, N-1, -1, i)

    print("#{} {}".format(tc, ans))