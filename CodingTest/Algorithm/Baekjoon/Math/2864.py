import sys
sys.stdin = open('input.txt')

A, B = input().split()

min_num = int(A.replace('6', '5')) + int(B.replace('6', '5'))
max_num = int(A.replace('5', '6')) + int(B.replace('5', '6'))

print(min_num, max_num)