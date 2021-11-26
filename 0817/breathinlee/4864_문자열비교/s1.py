import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    len1 = len(str1)
    len2 = len(str2)
    cnt = 0

    for i in range(len2-len1+1):
        for j in range(len1):
            if str2[i+j] != str1[j]:
                break
        else:
            cnt += 1

    print('#{} {}'.format(tc, cnt))