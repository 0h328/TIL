def solve():
    for i in range(N):                              # N행 만큼의 반복을 돌며
        for j in range(M-1, -1, -1):                # 끝에서부터(마지막은 1로 고정이니 M-1번부터) 0번째까지
            if arr[i][j] == '0': continue           # 0이면 넘어가고

            pwd = []                                # 1이면 대응하는 숫자를 담을 리스트 준비
            for pos in range(j-56 + 1, j, 7):       # 7개 영역에서
                pwd.append(P[arr[i][pos:pos+7]])    # i번 row의 pos~pos+7(-1) 범위의 col에 대응하는 이진코드를 찾아 대응하는 숫자를 넣자
            odd_digit_sum = pwd[0] + pwd[2] + pwd[4] + pwd[6]       # 홀수 자리 합
            even_digit_sum = pwd[1] + pwd[3] + pwd[5] + pwd[7]      # 짝수 자리 합
            if ((odd_digit_sum * 3 + even_digit_sum) % 10) == 0:    # 올바른 검증 코드 -> ((홀수 자리 합) * 3 + 짝수 자리 합) % 10 == 0 -> 10의 배수
                return odd_digit_sum + even_digit_sum               # 암호코드에 포함된 숫자들의 합 return
            else:                                                   # 검증코드가 틀린 경우 0 return
                return 0

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())     # N: 세로, M: 가로
    arr = [input() for _ in range(N)]    # 이진 암호 코드 입력
    P = {'0001101': 0,                   # 0 ~ 9까지의 수와 대응하는 이진 코드
         '0011001': 1,
         '0010011': 2,
         '0111101': 3,
         '0100011': 4,
         '0110001': 5,
         '0101111': 6,
         '0111011': 7,
         '0110111': 8,
         '0001011': 9}
    ans = solve()
    print('#{} {}'.format(tc, ans))