def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 시간이 매우 오래 걸림
import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    N = int(input())                          # 덤프 횟수
    boxes = list(map(int, input().split()))   # 박스 모음
    for _ in range(N):     # N번 덤프
        bubble_sort(boxes) # 정렬 (버블 정렬 활용)
        boxes[0] += 1      # 처음과 끝을 계속 평탄화
        boxes[-1] -= 1

    bubble_sort(boxes)     # 덤프 이후 최종 정렬
    ans = boxes[-1] - boxes[0]
    print('#{} {}'.format(tc, ans))