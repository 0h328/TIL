import sys
sys.stdin = open('input.txt')

for TC in range(1, int(input())+1):
    N, M = map(int, input().split())    # M : 47
    result = 'ON'
    len_bin = len(bin(M)[2:])           # 101111
    if len_bin < N:
        result = 'OFF'
    else:
        for i in range(len_bin-1, len_bin-1-N, -1):
            if bin(M)[2:][i] != '1':   # 1이 아니면
                result = 'OFF'
                break
    print('#{} {}'.format(TC, result))
