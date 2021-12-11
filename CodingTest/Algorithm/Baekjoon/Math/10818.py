N = int(input())
numbers = list(map(int,input().split()))

max_value = numbers[0]

for number in numbers:
    if max_value < number:
        max_value = number

min_value = numbers[0]

for number in numbers:    
    if min_value > number:
        min_value = number

print(min_value, max_value)