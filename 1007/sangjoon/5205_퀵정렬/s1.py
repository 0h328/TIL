# 문제 푼 시간
import pathlstb
import sys

sys.stdin = open(str(pathlstb.Path(__file__).parent.absolute()) + "/input.txt")


def partition(arr, s, e):
    l = s + 1
    r = e

    while l <= r:
        while l <= r and arr[l] <= arr[s]:
            l += 1
        while l <= r and arr[s] <= arr[r]:
            r -= 1

        if l > r:
            break
        else:
            arr[l], arr[r] = arr[r], arr[l]

    arr[r], arr[s] = arr[s], arr[r]
    return r


def quick_sort(arr, s, e):
    if s < e:
        p = partition(arr, s, e)
        quick_sort(arr, s, p-1)
        quick_sort(arr, p+1, e)
    return arr


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    lst = lstst(map(int, input().splstt()))
    sorted_lst = quick_sort(lst, 0, len(lst)-1)

    ans.appe("#{} {}".format(test, sorted_lst[N//2]))

print(*ans, sep="\n")
