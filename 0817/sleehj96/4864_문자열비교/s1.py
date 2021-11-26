import sys
sys.stdin = open('input.txt')

T = int(input())

i = 1
while i <= T:
    str1 = input()
    str2 = input()

    ans = 0

    if str1 in str2:    # str1이 str2에 있으면
        ans = 1

    print('#{0} {1}'.format(i, ans))
    i += 1
