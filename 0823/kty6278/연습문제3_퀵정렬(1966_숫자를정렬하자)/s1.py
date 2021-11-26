def quick_sort(x):
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quick_sort(less) + equal + quick_sort(more)

# 가변 배열
import sys
sys.stdin = open('input.txt')
nums = list(map(int, input().split()))
print(quick_sort(nums))