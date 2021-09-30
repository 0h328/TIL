import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    n, num = map(str, input().split())
    answer = ''

    for e in num:
        if e.isalpha():                     # A~F 이면 10~15로 변환
            e = ord(e) - ord('A') + 10
        e = int(e)                          # 문자열인 경우 int로 형변환

        e = bin(e)[2:]                      # 2진수로 만들고 앞에 0b 제거
        need = 4 - len(e)                   # 4글자로 맞추기 위하여 앞에 필요한 0의 갯수
        if need:
            e = '0' * need + e              # 앞에 0을 채워줌
        
        answer += e
    
    print('#{} {}'.format(tc, answer))