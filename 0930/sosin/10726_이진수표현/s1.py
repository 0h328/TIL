import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    N, M = map(int, input().split())
    print('#{} {}'.format((T+1), 'ON' if format(M, 'b')[-N:]=='1'*N else 'OFF'))

#1 OFF
#2 OFF
#3 ON
#4 ON
#5 OFF