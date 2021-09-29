import sys
from collections import deque
sys.stdin = open('input.txt')


code_dict = {
    int('0001101', 2): 0,
    int('0011001', 2): 1,
    int('0010011', 2): 2,
    int('0111101', 2): 3,
    int('0100011', 2): 4,
    int('0110001', 2): 5,
    int('0101111', 2): 6,
    int('0111011', 2): 7,
    int('0110111', 2): 8,
    int('0001011', 2): 9,
}


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    bin_code = ''
    arr = deque()
    answer = 0

    for _ in range(N):
        temp = input().strip('0')

        if temp:
            bin_code = temp
    # print('LOG --- BIN_CODE : {}'.format(bin_code))

    for i in range(8):
        end = len(bin_code) - (i*7)
        start = end - 7

        if start < 0:
            start = 0

        n = code_dict[int(bin_code[start:end], base=2)]
        arr.appendleft(n)
    # print('LOG --- ARR : {}'.format(arr)

    for i in range(8):
        if i == 7:
            answer += arr[i]
        elif not i & 1:   # 짝수일때
            answer += arr[i] * 3
        else:
            answer += arr[i]
    
    if not answer % 10:
        answer = sum(arr)
    else:
        answer = 0
    

    print('#{} {}'.format(tc, answer))