import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    data = list(map(int, input()))

    check = [0] * 12

    for i in data:
        check[i] += 1

    idx = 0
    tri = run = 0
    while idx < 10:
        if check[idx] >= 3:
            check[idx] -= 3
            tri += 1
            continue
        if check[idx] >= 1 and check[idx + 1] >= 1 and check[idx + 2] >= 1:
            check[idx] -= 1
            check[idx + 1] -= 1
            check[idx + 2] -= 1
            run += 1
            continue
        idx += 1

    if tri + run == 2:
        print('#{} {}'.format(case + 1, 1))
    else:
        print('#{} {}'.format(case + 1, 0))