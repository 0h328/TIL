import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    result = 0
    a_list = []

    for i in range(n-m+1):
        a_list.append(sum(a[i:m+i]))

    result = max(a_list) - min(a_list)

    print('#{} {}'.format(tc, result))