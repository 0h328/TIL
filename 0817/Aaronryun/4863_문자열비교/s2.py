import sys

sys.stdin = open('input.txt')

T = int(input())

for test in range(T):
    p = input()
    t = input()
    i = 0
    j = 0
    while j < len(p) and i < len(t):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
    if j == len(p):
        print('#{} {}'.format(test + 1, 1))
    else:
        print('#{} {}'.format(test + 1, 0))
