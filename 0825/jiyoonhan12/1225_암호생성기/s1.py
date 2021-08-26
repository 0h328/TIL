import sys
sys.stdin = open('input.txt')

def cycle(numbers):
    for i in range(1, 6):
        first = numbers.pop(0)
        f_change = first - i
        if f_change <= 0:
            f_change = 0
            numbers.append(f_change)
            return numbers
        numbers.append(f_change)
    cycle(numbers)

for t in range(1, 11):
    N = int(input()) # not used
    numbers = list(map(int, input().split()))
    new_numbers = []
    temp = (min(numbers) // 15) - 1 # 똑같은 숫자 빼줘도 되는 거 15 기준
    for num in numbers:
        new_numbers.append(num - (temp * 15))
    cycle(new_numbers)
    print('#{} '.format(t), end='')
    print(*new_numbers)