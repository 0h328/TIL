import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N, pw = input().split()

    s = []
    for i in range(len(pw)):
        s.append(pw[i])
        if len(s) > 1 and s[-1] == s[-2]:
            s.pop()
            s.pop()
    print('#{} {}'.format(tc, ''.join(s)))