import sys
sys.stdin = open('input.txt')


def cal(num, cal_list):
    global cnt
    if cal_list[-1] == 0:
        num += 1
    elif cal_list[-1] == 1:
        num -= 1
    elif cal_list[-1] == 2:
        num *= 2
    else:
        num -= 10

    if num == M:
        if cnt > len(cal_list):
            cnt = len(cal_list)
        return

    for i in [0, 1, 2, 3]:
        cal(num, cal_list+[i])

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    cnt = 987654321
    cal(N, [0])
