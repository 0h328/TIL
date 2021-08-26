import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))

    idx = M % N
    print('#{} {}'.format(tc+1, num[idx]))