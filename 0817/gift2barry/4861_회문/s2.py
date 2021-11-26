import sys
sys.stdin = open('input.txt')

# thought process: 소요시간 3분39초
# 행 에서 회문 탐색
# 열 에서 회문 탐색
# 하나씩 탐색

# 소요시간 21분 11초
def checker():                          # 회문 체크 함수
    for i in range(arr_len):                    # 문자열 리스트의 길이만큼 반복 (행, 열을 동시에 검사하기 때문)
        for j in range(arr_len - t_len+1):      # 주어진 문자열 안에서 회문의 길이를 고려하여 반복 검사
            if row[i][j:t_len+j] == row[i][j:t_len+j][::-1]:    # 행 에서 회문의 길이만큼의 문자열을 뒤집어보고 일치하면,
                ans = row[i][j:t_len+j]                         # 회문 발견, 바로  return
                return ans
            elif col[i][j:t_len+j] == col[i][j:t_len+j][::-1]:  # 열 에서 회문의 길이만큼의 문자열을 뒤집어보고 일치하면,
                ans = col[i][j:t_len+j]                         # 회문 발견, 바로 return
                return ans

for tc in range(1, int(input())+1):
    arr_len, t_len = map(int, input().split())  # 문자열 리스트의 길이, 회문의 길이 인풋값
    row = [input() for _ in range(arr_len)]     # 행 인풋값들
    c = list(zip(*row))
    col = [''.join(x) for x in c]               # 열 인풋값들 (다루기 쉽게 정돈됨)
    print('#{} {}'.format(tc, checker()))       # 정답 프린트


