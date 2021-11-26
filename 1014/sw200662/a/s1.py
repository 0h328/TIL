import sys

sys.stdin = open('input.txt')


def run1(a):
    global ans
    if a == N:
        print(ans)
        return

    for i in range(1,7):
        if a == 0:
            ans = str(i)
            run1(a+1)
            ans = ''
        else:
            temp2 = ans
            ans += ' '
            ans += str(i)
            run1(a+1)
            ans = temp2


def run2(a):
    pass


def run3(a):
    pass


N,M = map(int,input().split())
dice = ['1', '2', '3', '4', '5', '6']
ans = ''
run1(0)