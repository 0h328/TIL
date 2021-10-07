import sys
sys.stdin = open('input.txt')

def partition(A, l, r):
    pivot = A[l]
    i = l + 1
    j = r
    res = False
    while not res:
        while i <= j and pivot >= A[i]:
            i += 1
        while i <= j and pivot <= A[j]:
            j -= 1
        if i > j:
            res = True
        else:
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]
    return j

def quick_sort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quick_sort(A, l, s-l)
        quick_sort(A, s+l, r)

arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(arr, 0, len(arr)-1)
print(arr)