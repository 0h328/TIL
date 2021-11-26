import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    str1 = set(input())
    str2 = input()
    max_cnt = 0

    for char1 in str1:
        cnt = 0
        for char2 in str2:
            if char1 == char2:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

    print('#{} {}'.format(t, max_cnt))
