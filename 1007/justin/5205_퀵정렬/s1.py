def partition(arr, start, end):
    pivot = arr[start]                                      # 가장 왼쪽 요소를 pivot으로 설정
    left = start + 1                                        # pivot 다음 값을 left pointer
    right = end                                             # 가장 끝 값을 right pointer
    done = False

    while not done:
        while left <= right and arr[left] <= pivot:         # pivot보다 큰 값을 만날 때까지
            left += 1                                       # left를 오른쪽으로 이동 시키자
        while left <= right and pivot <= arr[right]:        # pivot보다 작은 값을 만날 때까지 반복
            right -= 1                                      # right를 왼쪽으로 이동 시키자
        if right < left:                                    # 만약 left가 더 크다면(=> left와 right 포인트가 크로스가 되었다면) -> 최종적으로 pivot과 right 교환(while문 탈출 이후)
                                                            # left, right 포인트가 교차하면 left, right는 pivot값을 기준으로 작은/큰 값의 경계에 위치
            done = True                                     # 반복 종료
        else:                                               # 아니라면
            arr[left], arr[right] = arr[right], arr[left]   # 왼쪽 & 오른쪽 교환
    arr[start], arr[right] = arr[right], arr[start]         # start(pivot)와 right의 요소 교환 -> pivot 위치 선정 완료(pivot 기준 왼쪽은 작은/오른쪽은 큰 값들로 구성)
    return right                                            # right는 이전 pivot(start)을 의미 -> 반환 -> 이후에 이 값을 기준으로 큰 / 작은으로 구역 분할

def quick_sort(arr, start, end):
    if start < end:                                         # 교차하지 않는다면
        pivot = partition(arr, start, end)                  # pivot 설정하고
        quick_sort(arr, start, pivot-1)                     # 왼쪽 정렬 -> pivot을 기준으로 그보다 작은 값으로 다시 분할 & 정렬
        quick_sort(arr, pivot+1, end)                       # 오른쪽 정렬 -> pivot을 기준으로 큰 값으로 다시 분할 & 정렬
    return arr

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    sorted_nums = quick_sort(nums, 0, len(nums)-1)          # 정렬 할 배열, 시작 idx, 끝 idx
    print('#{} {}'.format(tc, sorted_nums[N//2]))