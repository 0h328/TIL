import sys
sys.stdin = open('input.txt')

def quicksort(x):
    #Base Case
    if len(x) <= 1:
        return x            # 배열 반환

    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []

    for e in x:
        if e < pivot:
            less.append(e)
        elif e > pivot:
            more.append(e)
        elif e == pivot:
            equal.append(e)

    return quicksort(less) + equal + quicksort(more)



'''
def quicksort(x):
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

    return quicksort(less) + equal + quicksort(more)
'''

nums = list(map(int, input().split()))
print(quicksort(nums))