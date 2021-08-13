import sys
sys.stdin = open('input.txt')

def selection_sort(numbers):
    for i in range(len(numbers)-1):
        min_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers

numbers = list(map(int, input().split()))
print(numbers)
print(selection_sort(numbers))