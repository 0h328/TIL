import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range (T):
    C = input()
    cnt_mak = 0 # 파이프의 숫자
    ans = 0 # 잘린후 숫자
    for k in range(len(C)-1):
        if C[k] == '(' and C[k+1] == ')':
            ans += cnt_mak

        if C[k] == '(' and C[k+1] == '(':
            cnt_mak += 1
            ans += 1

        if C[k] == ')' and C[k+1] == ')':
            cnt_mak -= 1

    print('#{} {}'.format(i+1,ans))



