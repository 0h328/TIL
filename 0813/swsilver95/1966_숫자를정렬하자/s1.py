import sys

sys.stdin = open('input.txt')

T = int(input())

def BubbleSort(numbers):
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    for number in numbers:
        print(number, end=' ')

for tc in range(1, T + 1):
    n = 5
    numbers = list(map(int, input().split()))
    print('#{}'.format(tc), end=' ')
    BubbleSort(numbers)  
    print()