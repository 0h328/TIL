import sys
sys.stdin = open('input.txt')

T = int(input())

def min_max(a):
    max_num = a[0]
    min_num = a[0]
    for num in a:
        if num > max_num:
            max_num = num
    for num in a:
        if num < min_num:
            min_num = num
    diff = max_num - min_num
    return diff

for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))
    ans = min_max(a)
    print('#{} {}'.format(tc, ans))
