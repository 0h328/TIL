import sys
sys.stdin = open('input.txt')

d1 = int(input())
d2 = int(input())

circle = 3.141592 * 2 * d2
square = 2 * d1

print(square + circle)