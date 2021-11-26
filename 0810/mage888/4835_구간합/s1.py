import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    temp = []

    for i in range(N-M+1):
        temp.append(sum(data[i:M+i]))

    print('#{} {}'.format(tc, max(temp)-min(temp)))