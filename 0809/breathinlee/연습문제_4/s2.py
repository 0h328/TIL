import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    numbers = input()
    cnt = [0] * 10

    triplet = 0
    run = 0
    for num in numbers:
        cnt[int(num)] += 1

    idx = 0
    while idx < 10:
        if cnt[idx] >= 3:
            triplet += 1
            cnt[idx] -= 3
            continue
        idx += 1

    idx = 0
    while idx < 8:
        if cnt[idx] >= 1 and cnt[idx+1] >= 1 and cnt[idx+2] >= 1:
            run += 1
            cnt[idx] -= 1
            cnt[idx+1] -= 1
            cnt[idx+2] -= 1
            continue
        idx += 1

    if triplet + run >= 2:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))