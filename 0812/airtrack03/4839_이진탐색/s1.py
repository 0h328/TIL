import sys
sys.stdin = open('input.txt')

T = int(input())

def selection_sort(end_page, target):
    start = 1
    end = end_page
    cnt = 0
    while start <= end:
        mid = int((start + end) / 2)
        cnt += 1
        if mid == target:
            return cnt
        elif mid < target:
            start = mid
        else:
            end = mid

for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    cnt_A = selection_sort(P, A)
    cnt_B = selection_sort(P, B)

    if cnt_A > cnt_B:
        ans = 'B'
    elif cnt_B > cnt_A:
        ans = 'A'
    else:
        ans = 0

    print('#{} {}'.format(tc, ans))