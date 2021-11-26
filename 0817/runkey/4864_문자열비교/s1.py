import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t + 1):
    str1 = input()
    str2 = input()
    if str1 in str2:
        result = 1
    else:
        result = 0

    print("#{0} {1}".format(tc, result))
