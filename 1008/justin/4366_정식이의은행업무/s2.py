def solve(binary, ternary):
    bint = 0                                                 # 2진수 -> 10진수
    for x in binary:
        bint = bint * 2 + int(x)
    binary_list = []                                         # 잘못 기억한 이진수 목록
    for i in range(len(binary)):
        binary_list.append(bint ^ (1 << i))                  # 2진수의 1비트씩 바꿔서 저장
    for i in range(len(ternary)):                            # 3진수에서 다른 두 수로 바꿔 볼 자리
        num1 = num2 = 0                                      # (x+1) % 3 / (x+2) % 3

        for j in range(len(ternary)):
            if i != j:                                       # 잘못 저장했다고 판단하지 않은 자리
                num1 = num1 * 3 + int(ternary[j])            # * 3 / 1의 자리 채우기
                num2 = num2 * 3 + int(ternary[j])            # * 3 / 2의 자리 채우기
            else:                                            # 잘못 저장됐다고 판단한 자리
                num1 = num1 * 3 + (int(ternary[j]) + 1) % 3  # 0 -> 1 1 -> 2 2 -> 0
                num2 = num2 * 3 + (int(ternary[j]) + 2) % 3  # 0 -> 2 1 -> 0 2 -> 1

        if num1 in binary_list:
            return num1
        if num2 in binary_list:
            return num2

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    binary = input()
    ternary = input()
    ans = solve(binary, ternary)
    print('#{} {}'.format(tc, ans))