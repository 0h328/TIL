import sys
sys.stdin = open('input.txt')

"""
먼저 길이가 가장 긴 것부터 시작
하나씩 안쪽을 비교해가면서 다르면 flag_list를 0, 같으면 1을 만듦
col_idx가 max_idx // 2와 같아지면 해당 글자 길이 출력
flag_list가 다 0이면 다시 1로 만들고, 글자 길이를 하나를 줄여서 0번째 인덱스부터 비교
0번째 인덱스부터 했을 때 모든 행이 다 안 되면 1번 인덱스로 넘어가서 다시 모든 행 비교
"""

for _ in range(10):
    t = int(input())
    result_list = []
    flag_list = []
    for _ in range(100):
        result_list.append(input())
        flag_list.append(1)

    max_idx = len(result_list) - 1

    cnt = 0
    col_idx = 0

    """
    1 2 3 4 5 6 7
    0:3 0 ~ max//2
    4:7 max//2 + 1 ~ max
    
    1 2 3 4 5 6
    0:3 0 ~ max//2
    3:6 max//2 ~ max - 1
    2 3 4 5 6 7
    1:4
    4:7
    
    1 2 3 4 5
    0:2 0 ~ max//2
    3:5 max//2 ~ max - 2
    2 3 4 5 6
    1:3
    4:6
    3 4 5 6 7
    2:4
    5:7
    """

    for row_idx in range(max_idx + 1):
        if col_idx % 2:
        if result_list[row_idx][col_idx + cnt:max_idx//2] != result_list[row_idx][max_idx//2 + 1:len(max_idx)]:
            flag_list[row_idx] = 0
        else:
            flag_list[row_idx] = 1
        if 1 not in flag_list:
            cnt += 1
            break
        if col_idx == (max_idx)//2:
            result = max_idx - cnt + 1
    print("#{0} {1}".format(t, result))


    # while i > 0:
    #     for row_cnt in range(len(result_list)):
    #         result = []
    #         for i in range(len(result_list)//2):
    #             if result_list[row_cnt][i] != result_list[row_cnt][max_idx - i]:
    #                 result = []
    #                 break
    #             else:
    #                 result.append(result_list[row_cnt][i:max_idx - i])
    #             if i == len(result_list)//2 - 1:
    #                 result.append(result_list[row_cnt][i])
    #     i -= 1
    # print("#{0} {1}".format(t, result))