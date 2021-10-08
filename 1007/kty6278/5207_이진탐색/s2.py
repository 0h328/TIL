import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cnt = 0
    for i in range(m):
        if b[i] in a:
            cnt += 1
    print('#{} {}'.format(tc+1, cnt))