import sys
sys.stdin = open('input.txt')

A = int(input())

for number in range(1, A+1):
    c = [0] * 6
    for i in range(6):
        c[number % 10] += 1
        number //= 10
        numbers = list(map(int, input()))
