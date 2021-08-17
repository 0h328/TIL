import sys
sys.stdin = open('input.txt')


test_case = int(input())

for tc in range(1, test_case+1):
    str1, str2 = input().split()
    answer = 0

    idx = 0
    while idx < len(str1):
        answer += 1
        if str1[idx:idx+len(str2)] == str2:
            idx += len(str2)
            continue
        idx += 1

    print('#{} {}'.format(tc, answer))