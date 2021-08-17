import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1, t+1):
    str1 = input()
    str2 = input()

    if str2.find(str1) > -1:
        print('#{} {}'.format(idx, 1))
    else:
        print('#{} {}'.format(idx, 0))