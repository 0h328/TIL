import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    leftover = M % N
    for i in range(leftover):
        popped = numbers.pop(0)
        numbers.append(popped)
    print('#{} {}'.format(t, numbers[0]))