# 퀵정렬 - 인덱스 활용

def partition(arr, start, end):
    pivot = arr[start]                                      # pivot은 시작값
    left = start + 1                                        # 왼쪽 포인터는 pivot 다음값
    right = end                                             # 가장 마지막 값
    done = False                                            # 포인터가 교차되는 지점을 체크하는 변수
    while not done:                                         # 진행 중
        while left <= right and arr[left] <= pivot:         # 포인터가 교차하지 않고 왼쪽 포인터에 해당하는 값이 pivot보다 작거나 같다면
            left += 1                                       # 왼쪽 포인터 증가
        while left <= right and pivot <= arr[right]:        # 포인터가 교차하지 않고 오른쪽 포인터에 해당하는 값이 pivot보다 크거나 같다면
            right -= 1                                      # 오른쪽 포인터 증가
        if right < left:                                    # 교차하면
            done = True                                     # 종료 시키자
        else:
            arr[left], arr[right] = arr[right], arr[left]   # 교차하지 않으면 교환
    arr[start], arr[right] = arr[right], arr[start]
    return right

def quick_sort(arr, start, end):
    if start < end:                             # 왼쪽이 더 작은 경우만 진행
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)
    return arr

numbers = [0, 55, 22, 33, 2, 1, 10, 26, 42]
# numbers = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

print('정렬 전')
print(numbers)

result = quick_sort(numbers, 0, len(numbers)-1)

print('---------------------------------')
print('정렬 후')
print(result)