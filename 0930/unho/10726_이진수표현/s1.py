import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    num = bin(M) 
    answer = 'OFF'
    
    num = num[-N:]

    for e in num:
        if e != '1':
            break
    else:
        answer = 'ON'

    print('#{} {}'.format(tc, answer))