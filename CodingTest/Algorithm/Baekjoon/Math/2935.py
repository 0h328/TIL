import sys
sys.stdin = open('input.txt')

A = int(input())
cal = input()
B = int(input())

print(A+B if cal == '+' else A*B)
