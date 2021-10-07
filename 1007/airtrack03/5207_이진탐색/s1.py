import sys

sys.stdin = open('input.txt')

T = int(input())

def binary_search(start, end, key):
    prev = -1   # 왼쪽 0 오른쪽 1
    while start <= end:
        mid = (start + end) // 2

        if A[mid] == key:
            return True
        elif A[mid] < key and prev != 1:
            start = mid + 1
            prev = 1
        elif A[mid] > key and prev != 0:
            end = mid - 1
            prev = 0
        else:
            return False
    return False


for tc in range(1, T + 1):
    N, M = map(int, input().split())

    A = sorted(list(map(int, input().split())))     # 정렬된 N개의 리스트
    B = list(map(int, input().split()))     # key

    ans = 0

    for key in B:
        if binary_search(0, N-1, key):
            ans += 1

    print('#{} {}'.format(tc, ans))