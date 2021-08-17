import sys

sys.stdin = open('input.txt')

for test in range(int(input())):
    target, pattern = input().split()

    answer = len(target) - (len(pattern) - 1) * target.count(pattern)

    print('#{} {}'.format(test + 1, answer))
