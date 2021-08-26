import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = input()
    cnt = [0] * 10
    for number in numbers:
        cnt[int(number)] += 1

    max_cnt = max(cnt)

    for i in range(9, -1, -1):
        if cnt[i] == max_cnt:
            max_idx = i
            break

    print('#{} {} {}'.format(tc, max_idx, max_cnt))