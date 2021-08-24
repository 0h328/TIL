import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    print('#{}'.format(tc), end=' ')
    print(*a)