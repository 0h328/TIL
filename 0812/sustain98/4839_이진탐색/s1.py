import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1, t+1):
    p, pa, pb = map(int, input().split())

    low_a, low_b = 1, 1
    high_a, high_b = p, p
    find_a, find_b = False, False

    while low_a <= high_a and low_b <= high_b:
        mid_a, mid_b = (low_a + high_a)//2, (low_b + high_b)//2

        if mid_a == pa:
            find_a = True
        elif mid_a > pa:
            high_a = mid_a
        else:
            low_a = mid_a

        if mid_b == pb:
            find_b = True
        elif mid_b > pb:
            high_b = mid_b
        else:
            low_b = mid_b

        if find_a or find_b:
            break

    if find_a and find_b:
        res = '0'
    elif find_a:
        res = 'A'
    else:
        res = 'B'
    print('#{} {}'.format(idx, res))