import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    str1 = input()
    str2 = input()
    idx = 0
    for idx in range(len(str2) - len(str1) + 1):
        if str2[idx] == str1[0]:
            if str2[idx:idx + len(str1)] == str1:
                print('#{} {}'.format(case+1, 1))
                break
    else:
        print('#{} {}'.format(case+1, 0))
