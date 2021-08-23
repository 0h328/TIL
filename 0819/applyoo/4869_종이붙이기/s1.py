import sys
sys.stdin = open('input.txt')


T = int(input())
DP = [0, 1, 3, 5] + [0] * 27

for i in range(4, 31):
    if i % 2:
        DP[i] = (DP[i-1]*2) - 1
    else:
        DP[i] = (DP[i-1]*2) + 1

for test in range(T):
    num = int(input())
    print('#{} {}'.format(test+1, DP[num//10]))
