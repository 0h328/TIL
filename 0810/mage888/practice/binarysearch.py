def binarysearch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end :
        middle = (start + end) // 2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

print(binarysearch([2,4,7,9,11,19,23], 10))