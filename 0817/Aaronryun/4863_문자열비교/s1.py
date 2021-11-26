import sys

sys.stdin = open('input.txt')


def KMP_pattern(pattern):
    P = len(pattern)
    j = 0
    result = [0 for _ in range(P)]
    for i in range(1, P):
        while j > 0 and pattern[i] != pattern[j]:
            j = result[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            result[i] = j
    return result


def KMP_search(target, pattern):
    P = len(pattern)
    T = len(target)
    j = 0

    source = KMP_pattern(pattern)
    for i in range(0, T):
        while j > 0 and target[i] != pattern[j]:
            j = source[j - 1]
        if target[i] == pattern[j]:
            if j == P - 1:
                return 1
            else:
                j += 1
    return 0


for test in range(int(input())):
    pattern = input()
    target = input()
    print('#{} {}'.format(test+1,KMP_search(target,pattern)))