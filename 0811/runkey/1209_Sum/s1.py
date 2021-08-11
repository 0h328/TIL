import sys
sys.stdin = open("input.txt")

for _ in range(10): #총 테스트 케이스
    t = input()
    result_list = []
    for _ in range(100): # 10줄의 입력
        result_list.append(list(map(int, input().split())))
    diagonal_sum = 0
    reverse_diagonal_sum = 0

    result = sum(result_list[0])
    for row in range(100):
        diagonal_sum += result_list[row][row]   # 대각선(\) 합
        reverse_diagonal_sum += result_list[99-row][row]    #대각선 역(/)의 합

        if row == 99:
            if result < diagonal_sum:
                result = diagonal_sum
            if result < reverse_diagonal_sum:
                result = reverse_diagonal_sum

        if(result < sum(result_list[row])):   #행의 합
            result = sum(result_list[row])
        col_sum = 0
        for col in range(100):                #열의 합
            col_sum += result_list[col][row]
        if(result < col_sum):
            result = col_sum

    print("#{0} {1}".format(t, result))