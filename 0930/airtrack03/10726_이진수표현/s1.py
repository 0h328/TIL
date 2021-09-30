import sys
sys.stdin = open('input.txt')

T = int(input())

def to_binary(num):
    result = ''
    for i in range(N-1, -1, -1):
        if num & (1 << i):
            result += '1'
        else:
            result += '0'
    return result

for tc in range(1, T+1):
    N, M = map(int, input().split())

    result = to_binary(M)
    if result == '1' * N:
        ans = 'ON'
    else:
        ans = 'OFF'
    print('#{} {}'.format(tc, ans))