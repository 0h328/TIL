import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    num = int(input())
    number = list(map(int, input().split()))
    number.sort()
    # print(number)
    print('#{}'.format(t + 1), end = ' ')
    print(*number)
