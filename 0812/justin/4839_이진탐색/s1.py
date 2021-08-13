def binary_search(a, key, page):
    start = 1
    end = page
    cnt = 0
    while start <= end:
        middle = (start + end) // 2 # 절반
        cnt += 1
        if key == a[middle]:    # 페이지를 찾으면
            return cnt          # 그 페이지 반환
        elif key < a[middle]:   # 찾으려는 페이지가 end보다 작은 경우
            end = middle        # end를 옮기고
        else:                   # end보다 큰 경우
            start = middle      # start를 옮기자
    return False                # 검색실패

arr = [0] * 1001
for i in range(1, 1001):
    arr[i] = i

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    ans = '0'
    P, A, B = map(int, input().split())

    a = binary_search(arr, A, P)
    b = binary_search(arr, B, P)

    if a > b:
        ans = 'B'
    elif a < b:
        ans = 'A'
    else:
        ans = '0'

    print('#{} {}'.format(tc, ans))