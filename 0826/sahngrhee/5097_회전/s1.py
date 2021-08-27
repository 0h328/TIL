import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    for _ in range(M):
        numbers.append(numbers.pop(0))

    ans = numbers[0]
    print('#{} {}'.format(test_case, ans))
