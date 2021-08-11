import sys
sys.stdin = open('input.txt')

N = M = 100
T = 10
for test_case in range(1, T+1):
    tc = int(input())
    numbers = [list(map(int,input().split())) for _ in range(N)] # 2차원 배열을 만들기 위한 식
    # print(tc)
    # print(numbers)

    total_list = []                                     # 행, 열, 대각선의 합 최댓값을 구하므로, 하나의 리스트에 모아도 무관

# ------- 행 우선 순회 ------- #

    for i in range(len(numbers)):
        sum_row = 0                                     # 하나의 행을 합했으니, 다른 행을 합하기 위해서 행 위치에 초기화 변수 설정
        for j in range(len(numbers[i])):
            sum_row += numbers[i][j]
        total_list.append(sum_row)                      # total_list에 하나의 행을 합한 값 추가

# ------- 열 우선 순회 -------- #

    for i in range(len(numbers[i])):
        sum_col = 0                                     # 하나의 열을 합했으니, 다른 열을 합하기 위해 열 위치에 초기화 변수 설정
        for j in range(len(numbers)):
            sum_col += numbers[j][i]
        total_list.append(sum_col)                      # total_list에 하나의 열을 합한 값 추가

# ------- 정방향 대각 우선 순회 ------- #

    sum_op_angle = 0                                    # 정방향 대각선은 하나뿐이므로, 단일 for문 앞에 초기화 변수 설정
    for i in range(len(numbers)):                       # 정방향 대각선은 하나뿐이므로, 이중 for문 설정할 필요 없음
        sum_op_angle += numbers[i][i]                   # 위에 주석에 대한 설명은 해당 줄로 설명 가능
    total_list.append(sum_op_angle)                     # total_list에 정방향 대각선을 합한 값 추가

# ------- 역방향 대각 우선 순회 ------- #

    sum_rvop_angle = 0                                  # 역방향 대각선은 하나뿐이므로, 단일 for문 앞에 초기화 변수 설정
    for i in range(len(numbers)):                       # 역방향 대각선은 하나뿐이므로, 이중 for문 설정할 필요 없음
        sum_rvop_angle += numbers[i][len(numbers)-1-i]  # 아래부터 역방향(/) 위치로 더하기 위해 index 설정
    total_list.append(sum_rvop_angle)                   # total_list에 역방향 대각선을 합한 값 추가

    max_value = total_list[0]                           # 동일한 최댓값일 경우, 하나의 값만 출력하므로 임의 요소로 설정 무관
    for k in total_list:                                # 모든 줄에 합산된 값이 모인 list를 for문을 통해 순환시킴
        if max_value < k:                               # max_value가 total_list 내 요소보다 작다면
            max_value = k                               # 꾸준히 갱신시켜서, 최댓값을 가지게끔 만듦

    print('#{} {}'.format(test_case, max_value))        # 출력