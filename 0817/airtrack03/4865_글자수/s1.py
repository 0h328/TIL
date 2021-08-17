import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = list(input())
    M = len(str2)
    str2.sort()

    str1 = list(set(str1))
    str1.sort()

    ans = 0

    for target in str1:
        try:
            idx = str2.index(target)
        except:
            continue
        else:
            cnt = 0
            for i in range(idx, M):
                if str2[i] != target:
                    break
                cnt += 1
            if ans < cnt:
                ans = cnt

    print('#{} {}'.format(tc, ans))

