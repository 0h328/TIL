import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    deci = float(input())
    binary = ''
    while True:                 # 2진수로 변환하자
        deci *= 2
        binary += str(deci)[0]  # 1.25의 제일앞수
        if deci > 1:
            deci -= 1           # 0.25
        elif deci == 1:         # 2곱한 값이 1이 되면 종료
            break
    if len(binary) > 12:
        binary = 'overflow'
    print('#{} {}'.format(tc, binary))






# print(2**-3)
# 0.125