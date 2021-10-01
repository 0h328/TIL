import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    bin_M = bin(M)[2:]
    if len(bin_M) < N:
        ans = 'OFF'
    else:
        for i in range(len(bin_M)-1, len(bin_M)-1-N, -1):
            if bin_M[i] != '1':
                ans = 'OFF'
                break
        else:
            ans = 'ON'

    print("#{} {}".format(test_case, ans))


