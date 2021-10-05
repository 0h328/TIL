import sys
sys.stdin = open('input.txt')

T = int(input())

def is_baby(cnt, idx):
    if (
        cnt[idx] >= 3 or
        (idx >= 2 and cnt[idx-2] and cnt[idx-1] and cnt[idx]) or
        (1 <= idx < 9 and cnt[idx-1] and cnt[idx] and cnt[idx+1]) or
        (idx < 8 and cnt[idx] and cnt[idx+1] and cnt[idx+2])
    ):
        return True
    else:
        return False


for tc in range(1, T+1):
    data = list(map(int, input().split()))
    N = len(data)

    cnt_1 = [0] * 10
    cnt_2 = [0] * 10

    for i in range(N):
        if i & 1:   # i 홀수 => 플레이어 2
            cnt_2[data[i]] += 1
            if is_baby(cnt_2, data[i]):
                ans = 2
                break
        else:   # i 짝수 => 플레이어 1
            cnt_1[data[i]] += 1
            if is_baby(cnt_1, data[i]):
                ans = 1
                break
    else:
        ans = 0

    print('#{} {}'.format(tc, ans))




