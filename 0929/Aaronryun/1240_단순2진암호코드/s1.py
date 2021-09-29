import sys

sys.stdin = open('input.txt')

decode = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
          '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}  # 모든 숫자는 1로끝남

for test in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]

    temp = ''
    for i in range(N):
        for j in range(M - 1, -1, -1):  # 뒤에서 부터 보면서
            if data[i][j] == '1':  # 1이 등장한다면 숫자가 존재
                temp = data[i][j - 55:j + 1]  # 56개 숫자 잘라내기
                break
    result = []

    for i in range(0, 56, 7):  # 8개씩 자른다
        result.append(decode[temp[i:i + 7]])

    check = (result[0] + result[2] + result[4] + result[6]) * 3 + result[1] + result[3] + result[5] + result[7]

    if not check % 10:  # 유효한 수라면
        print('#{} {}'.format(test, sum(result)))
    else:  # 아니라면
        print('#{} {}'.format(test, 0))
