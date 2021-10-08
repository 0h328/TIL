import sys
sys.stdin = open('input.txt')


def quick_sort(s, e):
    if s >= e:
        return

    p = arr[s]
    l, r = s + 1, e
    while r >= l:
        while l <= r and p >= arr[l]:
            l += 1
        while l <= r and p <= arr[r]:
            r -= 1

        if r >= l:
            arr[l], arr[r] = arr[r], arr[l]

    arr[s], arr[r] = arr[r], arr[s]

    quick_sort(s, r-1)
    quick_sort(r+1, e)


ans = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(0, len(arr)-1)
    ans.append('#{0} {1}'.format(tc, arr[N//2]))

print(*ans, sep='\n')
