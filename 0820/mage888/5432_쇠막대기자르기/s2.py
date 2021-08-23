import sys
sys.stdin = open('input.txt')

def cut_Fe():

    global cnt

    for i in range(len(Fe)):
        if Fe[i] == '(':
            s.append('(')
        else:
            s.pop()
            if Fe[i-1] == '(':
                cnt += len(s)
            else:
                cnt += 1

    return cnt

T = int(input())

for tc in range(1, T+1):
    Fe = input()
    s = []
    cnt = 0

    print('#{} {}'.format(tc, cut_Fe()))



