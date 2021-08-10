import sys

sys.stdin = open('input.txt')

a = list(map(int, input().split()))


def CountingSort(a):
    cnt = [0] * (max(a) + 1)
    for i in a:
        cnt[i] += 1

    for i in range(1, len(cnt)):
        cnt[i] += cnt[i - 1]
    my_sort = [0]*len(a)
    for i in range(len(a)-1, 0, -1):
        my_sort[cnt[a[i]]-1] = a[i]
        cnt[a[i]] -= 1

    return my_sort


print(CountingSort(a))
