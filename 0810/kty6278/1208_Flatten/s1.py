import sys                                                   # input 데이터를 불러온다.
sys.stdin = open('input.txt')


for i in range(10):                                          # 10개의 테스트 케이스를 실행
    nums = int(input())                                      # 테스트 케이스 마다 덤프의 횟수를 받아온다.
    box_height = list(map(int, input().split()))             # 각 상자의 높이값을 받아온다.
    # print(nums, box_height)

    for _ in range(nums):                                  # 덤프의 수 'nums'만큼 반복
        max_box = max(box_height)                            # 상자의 높이 중 최대값
        min_box = min(box_height)                            # 상자의 높이 중 최소값
        index_max_box = box_height.index(max_box)            # 같은 값이 존재하는 경우, index를 이용해 높은 상자 중 가장 앞에 위치한 상자
        index_min_box = box_height.index(min_box)            # index를 이용해 가장 앞에 위치한 낮은 상자 높이의 위치
        box_height[index_max_box] -= 1                       # max 위치에 해당하는 상자 높이(= max 높이의 상자)에서 -1
        box_height[index_min_box] += 1                       # min 위치에 해당하는 상자 높이(= min 높이의 상자)에서 +1
    # print('#{} {}'.format(i+1, max_box - min_box)) -> testcase 1개 오류
    result = max(box_height) - min(box_height)
    print('#{} {}'.format(i + 1, result))

