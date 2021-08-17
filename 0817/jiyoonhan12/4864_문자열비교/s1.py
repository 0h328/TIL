import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2= input()
    # N, M = len(str1), len(str2)
    res = 0
    if str2.count(str1) > 0:
        res = 1
    print('#{} {}'.format(t, res))