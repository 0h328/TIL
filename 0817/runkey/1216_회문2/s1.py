import sys
sys.stdin = open('input.txt')

for _ in range(10):
    t = int(input())
    result_list = []
    for _ in range(100):
        result_list.append(input())
    row_idx = 0
    max_length = 0
    while row_idx < len(result_list):   # 100행
        row_length = len(result_list[row_idx])
        flag = 0
        for idx in range(row_length):    # 각 행의 맨 앞부터 하나씩 확인
            last = 0
            for last_idx in range(row_length):  # 처음과 마지막 문자 같은 순간 찾기
                if result_list[row_idx][idx] != result_list[row_idx][row_length - 1 - last_idx]:
                    continue
                else:

                    for col_idx in range(row_length):    # 하나씩 확인
                        if result_list[row_idx][idx + col_idx] != result_list[row_idx][row_length - 1 - last_idx - col_idx]:
                            break
                        if col_idx == (row_length - idx)//2:
                            if max_length < row_length - idx:
                                max_length = row_length - idx
                                flag = 1
                            break
                        if flag == 1:
                            break
        row_idx += 1
    result = max_length
    print("#{0} {1}".format(t, result))