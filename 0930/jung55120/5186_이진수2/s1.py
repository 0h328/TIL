import sys
sys.stdin = open('input.txt')

def binary(num):
    global text, cnt
    a = 1                      # a = 지수
    while num:                 # num이 0이 될 때까지 반복
        if num < 2 ** -a:      # ex. a가 1이면, 2의 -1제곱 -> 0.5보다 num이 작으면 else로
            text += '0'        # text에 0 붙여넣기
        else:                  # ex. a가 1일 때, 0.5보다 num이 크면
            num -= 2 ** -a     # num에서 2의 -1제곱만큼 빼주고
            text += '1'        # text에 1 붙여넣기
        cnt += 1               # 횟수 체크
        if cnt > 12:
            return 'overflow'  # 12번을 넘어서 overflow 출력
            break
        else:                  # 아니면 a에 숫자를 더해줌 (지수 1 올리기)
            a += 1
    return text


T = int(input())
for tc in range(1, T+1):
    num = float(input())
    text = ''                  # 2진수를 받아올 string
    cnt = 0                    # 횟수를 체크 (13번 이상은 overflow)
    print('#{} {}'.format(tc, binary(num)))