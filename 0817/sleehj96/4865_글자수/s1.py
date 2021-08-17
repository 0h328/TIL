import sys
sys.stdin = open('input.txt')

T = int(input())

i = 1
while i <= T:
    str1 = input()  # XYPV
    str2 = input()

    str1 = tuple(set(str1))
    cnt_list = [0] * len(str1)

    # for idx, e in enumerate(str1):  # X T P V를 하나씩 순회
    #     if e in str2:
    #         cnt_list[idx] = str2.count(e)

    for idx in range(len(str1)):
        for e in str2:
            if str1[idx] == e:
                cnt_list[idx] += 1

    print('#{0} {1}'.format(i, max(cnt_list)))
    # break
    i += 1