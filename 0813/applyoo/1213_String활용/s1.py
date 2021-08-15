import sys
sys.stdin = open('input.txt', encoding='UTF8')

def find_pattern(target, pattern):
    return target.count(pattern)


for _ in range(10):
    N = int(input())
    pattern = input()
    target = input()
    print('#{} {}'.format(N, find_pattern(target, pattern)))