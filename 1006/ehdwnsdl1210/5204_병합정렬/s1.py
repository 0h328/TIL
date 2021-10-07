'''
병합 정렬을 이용해 오름차순으로 정렬

정렬 된 결과만으로는 실제로 병합 정렬을 적용했는지 알 수 없기 때문에 다음과 같은 제약
N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할

병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력
정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력
'''

def merge_sort(array):
    global cnt

    if len(array) <= 1:
        return array

    mid = len(array) // 2

    low_array = merge_sort(array[:mid])
    high_array = merge_sort(array[mid:])


    merged_array = []

    l = h = 0

    if low_array[-1] > high_array[-1]:
        cnt += 1

    while l < len(low_array) and h < len(high_array):
        if low_array[l] <= high_array[h]:
            merged_array.append(low_array[l])
            l += 1

        else:
            merged_array.append(high_array[h])
            h += 1

    merged_array += low_array[l:]
    merged_array += high_array[h:]

    return merged_array


import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    cnt = 0

    arr = merge_sort(arr)

    print(f'#{tc} {arr[N//2]} {cnt}')

#1 2 0
#2 6 6