import sys
sys.stdin = open('input.txt')

t = int(input())

for num in range(1, t+1):
    n = int(input())
    dp = [0]*5001
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            dp[i] += 1

    p = int(input())
    print('#{}'.format(num), end=' ')
    for _ in range(p):
        print(dp[int(input())], end=' ')
    print()

    #완전 디피로 다시 풀기