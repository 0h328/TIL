import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = float(input())                          # 소수점 아래 12자리 이내인 N (float)
    result = ''                                 # 빈 문자열 생성
    cnt = 0                                     # 자릿수 기록
    print('#{}'.format(tc), end=' ')

    while N != 0 and cnt < 13:                  # 0이거나 13자리 이상이 되기 전까지 반복
        N *= 2                                  # 2를 곱하고
        cnt += 1                                # 자릿수 카운트
        if N >= 1:                              # 2를 곱한 값이 1이상이면 현재 자리수 1
            result += '1'                       # 1을 써부고
            N -= 1                              # 해당 자릿수를 1을 빼주자
        else:                                   # 2를 곱해서 1미만이면
            result += '0'                       # 현재 자리수 0 추가

    if cnt <= 12:                               # 12자리 이하인 경우 -> 결과 출력
        print(result)
    else:                                       # 12자리 이내로 표현할 수 없는 수 -> overflow 출력
        print('overflow')
