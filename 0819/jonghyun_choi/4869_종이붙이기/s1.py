import sys
sys.stdin = open('input.txt')

T = int(input())

def count_size(n):
    if n < 20:
        return 1
    return count_size(n-10) + count_size(n-20) * 2


for case in range(T):
    N = int(input())
    print('#{} {}'.format(case + 1, count_size(N)))