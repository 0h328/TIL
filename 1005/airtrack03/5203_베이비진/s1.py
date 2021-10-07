import sys
sys.stdin = open('input.txt')

T = int(input())

<<<<<<< HEAD
def is_baby(cnt, idx):
    if (
        cnt[idx] >= 3 or
        (idx >= 2 and cnt[idx-2] and cnt[idx-1] and cnt[idx]) or
        (1 <= idx < 9 and cnt[idx-1] and cnt[idx] and cnt[idx+1]) or
        (idx < 8 and cnt[idx] and cnt[idx+1] and cnt[idx+2])
=======
def is_baby(cnt, idx, is_odd):
    if (
        cnt[idx][is_odd] >= 3 or
        (idx >= 2 and cnt[idx-2][is_odd] and cnt[idx-1][is_odd]) or
        (1 <= idx < 9 and cnt[idx-1][is_odd] and cnt[idx+1][is_odd]) or
        (idx < 8 and cnt[idx+1][is_odd] and cnt[idx+2][is_odd])
>>>>>>> 0f3d00a6e1043fba483b14d316abf1af9418f6a3
    ):
        return True
    else:
        return False


for tc in range(1, T+1):
    data = list(map(int, input().split()))
    N = len(data)

<<<<<<< HEAD
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
=======
    cnt = [[0] * 2 for _ in range(10)]

    for i in range(N):
        cnt[data[i]][i&1] += 1
        if is_baby(cnt, data[i], i&1):
            ans = (i&1) + 1
            break
>>>>>>> 0f3d00a6e1043fba483b14d316abf1af9418f6a3
    else:
        ans = 0

    print('#{} {}'.format(tc, ans))




