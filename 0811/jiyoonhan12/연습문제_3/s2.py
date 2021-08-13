import sys
sys.stdin = open('input2.txt')

numbers = list(map(int, input().split()))

for i in range(1, 1 << len(numbers)):
    for j in range(len(numbers)):
        if i & (1 << j):
            print(numbers[j], end=' ')
    print()