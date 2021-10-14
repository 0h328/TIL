import sys
sys.stdin = open('input.txt')


def cal(num):
    global cnt, ans
    if num > M+1:
        return

    if num == M:
        if ans > cnt:
            ans = cnt

    for i in range(4):
        if i == 0:
            cnt += 1
            cal(2 * num)
        else:
            if num+pluses[i] == M:
                cnt += 1
                return
            else:
                cnt += 2
                cal(2*(num+pluses[i]))

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    temp = N
    cnt_2 = 0
    while temp < M:
        temp *= 2
        cnt_2 += 1
    ans = 987654321
    cnt = 0
    pluses = {0: 0, 1: 1, 2: -1, 3: -10}
    cal(N)