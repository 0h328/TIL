import sys
sys.stdin = open('input.txt')

x = [int(input()) for _ in range(3)]

if sum(x) != 180:
    print("Error")
elif x[0] == x[1] == x[2]:
    print("Equilateral")
elif x[0] != x[1] and x[0] != x[2] and x[1] != x[2]:
    print("Scalene")
else:
    print("Isosceles")