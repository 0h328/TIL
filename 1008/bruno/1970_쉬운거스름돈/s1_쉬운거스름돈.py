import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans = [0] * 8
    for i in range(8):
        if N//won[i]:
            ans[i] = N // won[i]
            N = N % won[i]
    print('#{}'.format(t))
    print(*ans)