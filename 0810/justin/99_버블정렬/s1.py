#1. 정렬 - O(N^2)
def bubble_sort(arr):
    # len(arr)이 아닌 len(arr)-1인 이유는 j+1에서 index error를 막기 위함
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


#2. 최적화된 버블 정렬
def optimized_bubble_sort(arr):
    for i in range(len(arr)):
        swapped = True
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = False
        # 만약 마지막 swap에서 swap이 일어나지 않으면
        # 이미 정렬되어 있다는 의미 -> break 
        # 더 이상 불필요하게 볼 필요가 없음
        if swapped:
            break

# 정렬 -> 최대 - 최소
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # bubble_sort(numbers)
    optimized_bubble_sort(numbers)
    ans = numbers[N-1] - (-numbers[0])
    print('#{} {}'.format(tc, ans))

# 참고 -> 단순 반복문 -> O(N)
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int, input().split()))

#     min_value = 987654321
#     max_value = 0

#     for i in range(N):
#         if max_value < numbers[i]:
#             max_value = numbers[i]

#         if min_value > numbers[i]:
#             min_value = numbers[i]
#     print('#{} {}'.format(tc, max_value - min_value))