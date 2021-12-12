import sys
sys.stdin = open('input.txt')

while True:
    numbers = list(map(int, input().split()))

    if sum(numbers) == 0:
        break

    max_number = max(numbers)
    numbers.remove(max_number)

    if numbers[0]**2 + numbers[1]**2 == max_number**2:
        print('right')
    else:
        print('wrong')