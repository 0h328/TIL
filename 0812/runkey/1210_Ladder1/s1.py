import sys
sys.stdin = open("input.txt")

for _ in range(10):                                         # 테스트 케이스 10번 반복
    result = []                                             # 100 x 100 사다리 정보 리스트를 담음
    t = int(input())                                        # 해당 테스트 케이스 번호
    for i in range(100):                                    # 100줄 입력
        result.append(list(map(int, input().split())))      # 100줄 입력 받음

    end_row = len(result) - 1                               # result 길이에서 1줄을 뺌 (0~99이기 때문)
    end_col = result[end_row].index(2)                      # 마지막 줄에서 숫자 2를 찾음
    end_row -= 1                                            # row를 한 줄 뺌
    flag = 0                                                # 어느 쪽으로 움직일지 정하는 변수
    while end_row >= 0:                                     # row가 0번째 줄 이상이면 작동
        if end_row == 0:                                    # row가 0번째 줄이면
            result_col = end_col                            # result_col에 end_col을 담음
            break                                           # 종료

        # flag가 0이면 사다리 좌우 정보를 파악하고, 1이 아니면 row를 1 빼줌
        if flag == 0:
            # 0열이면서 우측 사다리 정보가 0 이거나 99열이면서 좌측 사다리 정보가 0이면 row를 1 빼줌
            if ((end_col == 0) and (result[end_row][end_col + 1] == 0))\
                or ((end_col == 99) and (result[end_row][end_col - 1] == 0)):
                end_row -= 1

            # 0열이 아니면서 좌측 정보가 1이면 열을 1 빼주고 flag를 -1을 줌
            # (result[end_row][-1]은 마지막 열을 가리키기에 0열을 제외시킨 것임
            elif (end_col != 0) and (result[end_row][end_col - 1] == 1):
                end_col -= 1
                flag = -1

            # 99열이 아니면서 우측 정보가 1이면 열을 1 더해주고 flag를 1을 줌
            # (result[end_row][100]은 인덱스 초과가 나서 100열을 제외시킨 것임
            elif (end_col != 99) and result[end_row][end_col + 1] == 1:
                end_col += 1
                flag = 1

            # 좌우측 사다리 정보가 0이면
            else:
                end_row -= 1

        elif flag == -1:                                # flag가 -1이면
            while(result[end_row - 1][end_col] == 0):   # 위칸의 정보가 0일 동안에
                end_col -= 1                            # col을 1 빼줌
            end_row -= 1                                # row를 1 빼줌
            flag = 0                                    # flag를 0으로 만듦

        elif flag == 1:                                 # flag가 1이면
            while(result[end_row - 1][end_col] == 0):   # 위칸의 정보가 0일 동안에
                end_col += 1                            # col을 1 더해줌
            end_row -= 1                                # row를 1 빼줌
            flag = 0                                    # flag를 0으로 만듦

    print("#{0} {1}".format(t, result_col))             # 현재 테스트 케이스와 최종 열을 구함