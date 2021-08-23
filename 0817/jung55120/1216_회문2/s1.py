import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    n = 100

    row_str_list = [list(input()) for _ in range(n)]
    col_str_list = list(zip(*row_str_list))
    print(row_str_list)

    result = 0

    for length in range(n, 0, -1): # 회문의 길이를 기준으로
        for i in range(n - length + 1): # 시작점의 위치를 한 칸씩 옮기기 위함(index error를 고려)
            for y in range(n):  # index of row and col # 모든 행과 열을 다 체크한다.
                if row_str_list[y][i: i + length] == row_str_list[y][i: i + length][::-1]:
                    result = length
                    break
                elif col_str_list[y][i: i + length] == col_str_list[y][i: i + length][::-1]:
                    result = length
                    break
            if result > 0:
                break
        if result > 0 :
            break
    print('#{0} {1}'.format(tc, result))

    #  cnt = 1 :
    #  length = 100, i = 0, y = 0
    #  row_str_list[0][0:100] == row_str_list[0][0:100][::-1] # 리스트를 뒤집는다는 뜻
    #  첫번째 행의 0~99까지의 원소들을 회문인지 판별

    #  cnt = 2 :
    #  length = 100, i = 0, y = 1
    #  row_str_list[1][0:100] == row_str_list[1][0:100][::-1] # 리스트를 뒤집는다는 뜻
    #  두번째 행의 0~99까지의 원소들을 회문인지 판별

    #  cnt = n :
    #  length = 57, i = 20, y = 1
    #  row_str_list[1][20:77] == row_str_list[1][20:77][::-1] # 리스트를 뒤집는다는 뜻
    #  n번째 행의 0~99까지의 원소들을 회문인지 판별


