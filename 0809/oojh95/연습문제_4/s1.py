import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    card_list = input()
    cnt = [0]*10

    triplet = 0
    run = 0
    for num in card_list:
        k = int(num) % 10
        cnt[k] += 1

    i = 0
    while i < 10:
        if cnt[i] >= 3:
            triplet += 1
            cnt[i] -= 3
            continue
        i += 1
    i = 0
    while i < 8:
        if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
            run += 1
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            continue
        i += 1
    if run + triplet >= 2:
        print('#{} 1'.format(test_case))
    else:
        print('#{} 0'.format(test_case))

