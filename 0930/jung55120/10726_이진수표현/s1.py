import sys
sys.stdin = open('input.txt')

def binery(n):
    output = ''
    for i in range(N):
        if n & (1 << i):        # 비트 연산자를 활용해서 체크
            output += '1'       # 해당하면 1을 추가
            n -= (1 << i)       # 체크 했으니까 2의 i제곱은 n에서 빼주기
        else:
            output += '0'
    return output

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    if binery(M) == '1' * N:
        print('#{} {}'.format(tc, 'ON'))
    else:
        print('#{} {}'.format(tc, 'OFF'))