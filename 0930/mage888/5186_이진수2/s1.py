import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    temp = ''
    while N:
        N *= 2
        temp += str(int(N))
        N -= int(N)

        if len(temp) >= 13:
            print('#{} overflow'.format(tc))
            break
    if N - int(N) == 0:
        print('#{} {}'.format(tc, temp))


