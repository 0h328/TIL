import sys
sys.stdin = open('input.txt')

def quick_sort(s, e):
    global l
    if s >= e:
        return
    pivot = s
    left = s + 1
    right = e
    while left <= right:
        if l[right] < l[pivot] < l[left]:
            l[left], l[right] = l[right], l[left]
        else:
            if l[left] <= l[pivot]:
                left += 1
            if l[right] >= l[pivot]:
                right -= 1
    l[right], l[pivot] = l[pivot], l[right]
    quick_sort(s, right-1)
    quick_sort(left, e)

t = int(input())
for idx in range(1, t+1):
    n = int(input())
    l = list(map(int, input().split()))

    quick_sort(0, n-1)

    print('#{} {}'.format(idx, l[n//2]))