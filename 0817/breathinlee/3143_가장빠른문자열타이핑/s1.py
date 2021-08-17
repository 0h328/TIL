import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    str1, str2 = input().split()

    cnt = 0
    idx1 = 0

    while idx1 < len(str1) - len(str2) + 1:
        for idx2 in range(len(str2)):
            if str1[idx1+idx2] != str2[idx2]:
                break
        else:
            cnt += 1
            idx1 = idx1 + len(str2) - 1
        idx1 += 1

    print('#{} {}'.format(tc, len(str1) - len(str2)*cnt + cnt))