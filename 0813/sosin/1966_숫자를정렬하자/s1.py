import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    input()
    numbers = list(map(int, input().split()))
    numbers.sort()
    print('#{}'.format((T+1)), end=' ')
    print(*numbers)