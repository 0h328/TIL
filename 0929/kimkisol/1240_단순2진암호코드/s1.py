import sys

sys.stdin = open('input.txt')
'''
 “(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드” 가 10의 배수가 되어야 한다.
'''


def Verify(code):  # 0번 인덱스 값
    check = 0
    result = 0
    for i in range(8):
        num = secret_code.index(code[7 * i:7 * i + 7])
        if i % 2 == 0:
            check += num * 3
        else:
            check += num
        result += num

    if check % 10 == 0:
        return result
    return 0


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())  # N: 행, M : 열
    input_code = [list(map(int, input())) for _ in range(N)]
    secret_code = [
        [0, 0, 0, 1, 1, 0, 1],  # 0
        [0, 0, 1, 1, 0, 0, 1],  # 1
        [0, 0, 1, 0, 0, 1, 1],  # 2
        [0, 1, 1, 1, 1, 0, 1],  # 3
        [0, 1, 0, 0, 0, 1, 1],  # 4
        [0, 1, 1, 0, 0, 0, 1],  # 5
        [0, 1, 0, 1, 1, 1, 1],  # 6
        [0, 1, 1, 1, 0, 1, 1],  # 7
        [0, 1, 1, 0, 1, 1, 1],  # 8
        [0, 0, 0, 1, 0, 1, 1],  # 9
    ]

    for i in range(N):
        for j in range(M):
            if input_code[i][j] == 1:
                code = input_code[i][j:j + 56]
                break

    while code[-1] == 0:
        code.insert(0, code.pop())

    print('#{}'.format(t), Verify(code))
