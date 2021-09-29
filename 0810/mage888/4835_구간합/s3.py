import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    temp = []
    for i in range(N-M+1):
        total = 0
        for j in range(i, i+M):
            total += numbers[j]
        temp.append(total)

    print('#{} {}'.format(tc, max(temp)-min(temp)))


