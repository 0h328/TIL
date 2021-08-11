import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    a_list = list(map(int, input().split()))    # 입력부분

    max_num = 0 # 최대값 초기화
    min_num = 1000001   #최소값 초기화
    for i in a_list:    # 리스트에 반복하며 최대값보다 크거나 최소값보다 작으면 갱신.
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    result = max_num - min_num  #결과

    print('#{} {}'.format(test_case, result))
