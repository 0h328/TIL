import sys
sys.stdin = open('input.txt')

# thought process: 소요시간 9분
# N 안에 M 길이 만큼의 문자열을 고지식 알고리즘으로 차례대로 확인
# 해당 문자를 슬라이싱 이용해 비교하여 같으면, 회문
# 아니라면 전체 문자열에서 인덱스 한칸 전진한 뒤 반복
# 세로 가로 둘 다 적용해서 해보자 while 문 이용하여 try

# 수민님 코드 참조
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


