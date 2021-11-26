import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    cnt = int(input())                          # 덤프 횟수
    height = list(map(int, input().split()))    # 100개 박스 높이 리스트

    while cnt:                                  # 덤프 횟수 만큼 반복
        max_height = min_height = height[0]     # 박스높이 최댓값, 최솟값 초기화
        max_idx = min_idx = 0                   # 최댓값, 최솟값의 인덱스 초기화

        for j in range(100):                    # max, min값과 index구하기
            if height[j] > max_height:
                max_height = height[j]
                max_idx = j
            elif height[j] < min_height:
                min_height = height[j]
                min_idx = j

        height[max_idx] -= 1                    # 최댓값 1 감소
        height[min_idx] += 1                    # 최솟값 1 증가
        cnt -= 1                                # 덤프 1회 감소

    height_gap = max(height) - min(height)      # 마지막 덤프 실행 후 다시 정렬
    print('#{} {}'.format(tc, height_gap))
