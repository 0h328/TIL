import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    maxi = 0
    mini = 10000*M

    for i in range(N-M+1):
        total = sum(numbers[i:M+i])
        if total > maxi:
            maxi = total
        if total < mini:
            mini = total

    print('#{} {}'.format(idx, maxi-mini))