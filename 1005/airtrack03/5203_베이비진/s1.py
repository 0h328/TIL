import sys
sys.stdin = open('input.txt')

T = int(input())

def is_baby(cnt, idx, is_odd):
    if (
        cnt[idx][is_odd] >= 3 or
        (idx >= 2 and cnt[idx-2][is_odd] and cnt[idx-1][is_odd]) or
        (1 <= idx < 9 and cnt[idx-1][is_odd] and cnt[idx+1][is_odd]) or
        (idx < 8 and cnt[idx+1][is_odd] and cnt[idx+2][is_odd])
    ):
        return True
    else:
        return False


for tc in range(1, T+1):
    data = list(map(int, input().split()))
    N = len(data)

    cnt = [[0] * 2 for _ in range(10)]

    for i in range(N):
        cnt[data[i]][i&1] += 1
        if is_baby(cnt, data[i], i&1):
            ans = (i&1) + 1
            break
    else:
        ans = 0

    print('#{} {}'.format(tc, ans))




