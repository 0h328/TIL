import sys
sys.stdin = open('input.txt')


def binary_search(num, start, end, chk):

    if start <= end:
        mid = (start+end) // 2

        if list_A[mid] == num:
            return True

        elif list_A[mid] < num:
            if chk == -1:
                return
            return binary_search(num, mid + 1, end, -1)

        else:
            if chk == 1:
                return
            return binary_search(num, start, mid-1, 1)


for tc in range(int(input())):
    N, M = map(int, input().split())
    list_A = list(map(int, input().split()))
    list_B = list(map(int, input().split()))

    list_A.sort()
    ans = 0
    for b in list_B:
        if binary_search(b, 0, N-1, 0):
            ans += 1
    print('#{0} {1}'.format(tc+1, ans))
    # break
