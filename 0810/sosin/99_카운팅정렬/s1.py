def counting_sort(arr):
    k = max(arr)+1
    length = len(arr)
    counting_list = [0]*k
    for i in arr:
        counting_list[i]+=1
    
    for i in range(1, k):
        counting_list[i] += counting_list[i-1]

    result = [0]*length
    # 안정 정렬 (stable sort)
    # [(1,3), (2,1), (1,5)]
    # (1,3) (1,5) (2,1)
    # (1,5) (1,3) (2,1)
    for i in range(length-1, -1, -1):
        counting_list[arr[i]]-=1
        idx = counting_list[arr[i]]
        result[idx] = arr[i]
    return result


print(counting_sort([3,4,6,6,3,3,2,5,6]))
