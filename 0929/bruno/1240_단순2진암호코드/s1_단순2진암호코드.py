import sys
sys.stdin = open('input.txt')


def check(code):
    temp = 0    # 10의 배수인지 체크할 임시변수
    result = 0  # 변환한 코드의 합
    for i in range(8):
        # 01110110110001011101101100010110001000110100100110111011
        num = change.index(code[7*i:7*i+7])
        if i % 2 == 0:
            temp += num * 3
        else:
            temp += num
        result += num
    if temp % 10:
        return 0
    return result


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    input_code = [input() for _ in range(N)]
    change = ['0001101', '0011001', '0010011', '0111101', '0100011',
              '0110001', '0101111', '0111011', '0110111', '0001011']

    for i in range(N):
        for j in range(M-1, -1, -1):
            if input_code[i][j] == '1':
                code = input_code[i][j-55:j+1]
                break
    # print(code)
    # 01110110110001011101101100010110001000110100100110111011
    print('#{} {}'.format(tc, check(code)))
