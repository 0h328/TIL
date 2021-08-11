def get_min_idx():
    min_value = 987654321
    min_idx = -1

    for i in range(len(boxes)):  # 박스의 길이만큼 반복을 돌며 최저 높이를 찾자
        if boxes[i] < min_value: # i번째 박스의 높이가 내가 가진 박스보다 작으면 최솟값 및 idx 교체
            min_value = boxes[i]
            min_idx = i
    return min_idx

def get_max_idx():
    max_value = 0
    max_idx = -1

    for i in range(len(boxes)):  # 박스의 길이만큼 반복을 돌며 최저 높이를 찾자
        if boxes[i] > max_value: # i번째 박스의 높이가 내가 가진 박스보다 크면 최댓값 및 idx 교체
            max_value = boxes[i]
            max_idx = i
    return max_idx

import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    N = int(input())                         # 덤프 횟수
    boxes = list(map(int, input().split()))  # 박스 목록
    for _ in range(N):                       # N번 덤프하기
        boxes[get_max_idx()] -= 1            # 최고 높이 상자 한 칸 내리기
        boxes[get_min_idx()] += 1            # 최저 높이 상자 한칸 올리기
    ans = boxes[get_max_idx()] - boxes[get_min_idx()]  # 최고점과 최저점의 차이
    print('#{} {}'.format(tc, ans))