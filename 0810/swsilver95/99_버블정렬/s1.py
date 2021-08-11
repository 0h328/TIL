import sys
sys.stdin = open('input.txt')


numbers = list(map(int, input().split()))

def BubbleSort(numbers):
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


print(BubbleSort(numbers))
