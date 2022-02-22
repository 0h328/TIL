import sys
sys.stdin = open('input.txt')

N = int(input())

if N % 2:
    print("SK")
else:
    print("CY")