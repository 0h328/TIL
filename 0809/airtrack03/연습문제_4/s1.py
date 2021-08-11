import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    num = input()
    cnt = [0] * 10

    for n in num:
        cnt[int(n)] += 1

    for i in range(10):
        if cnt[i] % 3 == 0:
            cnt[i] = cnt[i] - 3 * (cnt[i]//3)

    for i in range(8):
        if cnt[i] == cnt[i+1] and cnt[i] == cnt[i+2] and cnt[i]:
            temp = cnt[i]
            cnt[i] -= temp
            cnt[i+1] -= temp
            cnt[i+2] -= temp

    if sum(cnt):
        ans = 0
    else:
        ans = 1

    print('#{} {}'.format(tc, ans))