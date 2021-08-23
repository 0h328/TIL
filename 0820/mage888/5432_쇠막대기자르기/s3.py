import sys

sys.stdin = open('input.txt')


def cut_Fe():

    global cnt
    ans = 0

    for i in range(len(Fe)):
        if Fe[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if Fe[i - 1] == '(':
                ans += cnt
            else:
                ans += 1
    return ans


T = int(input())

for tc in range(1, T + 1):
    Fe = input()
    s = []
    cnt = 0

    print('#{} {}'.format(tc, cut_Fe()))



