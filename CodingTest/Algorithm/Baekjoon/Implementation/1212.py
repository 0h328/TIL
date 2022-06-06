import sys
sys.stdin = open('input.txt')

print(bin(int(input(), 8))[2:])