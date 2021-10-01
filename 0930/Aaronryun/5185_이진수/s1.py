import sys

sys.stdin = open('input.txt')

for test in range(1, 1 + int(input())):
    N, num = input().split()
    answer = ''
    for i in range(int(N)):
        answer += '{0:04b}'.format(int(num[i], 16))
    print('#{} {}'.format(test, answer))
