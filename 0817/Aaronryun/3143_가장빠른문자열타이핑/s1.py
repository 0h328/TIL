import sys

sys.stdin = open('input.txt')


def KMP_pattern(pattern):
    P = len(pattern)
    result = [0 for _ in range(P)]
    j = 0
    for i in range(1, P):
        while j > 0 and pattern[i] != pattern[j]:
            j = result[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            result[i] = j
    return result


def KMP_search(target, pattern):
    T = len(target)
    P = len(pattern)
    source = KMP_pattern(pattern)
    j = 0
    cnt = 0
    for i in range(0, T):
        while j > 0 and target[i] != pattern[j]:
            j = source[j - 1]
        if target[i] == pattern[j]:
            if j == P - 1:
                cnt += 1
            else:

                j += 1
    return cnt


t = int(input())
for test in range(t):
    target, pattern = input().split()
    answer = len(target) - KMP_search(target, pattern) * (len(pattern) - 1)

    print('#{} {}'.format(test + 1, answer))
