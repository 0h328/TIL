import sys
sys.stdin = open('input.txt')


def isInclude(pattern, word):
    if pattern in word: # 패턴이 있는 경우
        return 1
    else: # 없는 경우
        return 0


T = int(input())
for test in range(T):
    str1 = input()
    str2 = input()

    print('#{} {}'.format(test+1, isInclude(str1, str2)))