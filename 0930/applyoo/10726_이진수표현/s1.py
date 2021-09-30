import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M  = map(int, input().split())
    ans = ''

    for i in range(N):  # N번만 반복
        if M and M % 2:  # M이 존재하고 나머지가 있는 경우
            M //= 2
        else:  # 없으면 OFF
            print('#{0} {1}'.format(tc, 'OFF'))
            break
    else:  # 정상 종료됐으면 ON
        print('#{0} {1}'.format(tc, 'ON'))
