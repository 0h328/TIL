import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())   # N : 글자판 크기, M : 회문의 길이

    row_str_list = [input() for _ in range(N)]
    # print(row_str_list)

    col_str_list = list(zip(*row_str_list))
    # print(col_str_list)

    palindrome_list = []

    # 행 순회
    for i in range(N):
        for j in range(N-M+1):
            if row_str_list[i][j:j+M] == row_str_list[i][j:j+M][::-1]:
                palindrome_list.append(row_str_list[i][j:j+M])
    # print(palindrome_list)

    # 열 순회
    for i in range(N):
        for j in range(N-M+1):
            if col_str_list[i][j:j+M] == col_str_list[i][j:j+M][::-1]:
                palindrome_list.append(''.join(col_str_list[i][j:j+M]))

    print('#{} {}'.format(tc, *palindrome_list))
