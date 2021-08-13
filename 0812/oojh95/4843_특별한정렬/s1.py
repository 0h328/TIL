import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N-1):
        idx = i
        for j in range(i + 1, N):
            if i % 2 == 0:
                if numbers[idx] < numbers[j]:
                    idx = j
            else:
                if numbers[idx] > numbers[j]:
                    idx = j
        numbers[i], numbers[idx] = numbers[idx], numbers[i]
    print('#{}'.format(test_case), end=' ')
    for i in range(9):
        print(numbers[i], end=' ')
    print(numbers[9])

