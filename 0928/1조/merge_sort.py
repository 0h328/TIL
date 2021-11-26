# arr = [5, 6, 3, 2, 1, 6, 7, 8, 22, 13, 25, 35, 12, 9999]
arr = list(range(16, 0, -1))
cnt = 0

def merge_sort(start, end):
    global cnt
    if end - start == 1:
        if arr[start] > arr[end]:
            arr[start], arr[end] = arr[end], arr[start]
            cnt += 1
        return 

    mid = (start + end) // 2

    merge_sort(start, mid)
    merge_sort(mid, end)

    left, right = start, mid
    merged = []
    while left < mid and right < end:
        if arr[left] > arr[right]:
            merged.append(arr[right])
            right += 1
        else:
            merged.append(arr[left])
            left += 1
        cnt += 1
    
    while right < end:
        merged.append(arr[right])
        right += 1

    while left < mid:
        merged.append(arr[left])
        left += 1

    arr[start:end] = merged


merge_sort(0, len(arr) - 1)
# print(arr)
print(cnt)