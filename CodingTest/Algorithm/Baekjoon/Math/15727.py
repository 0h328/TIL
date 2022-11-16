import sys
sys.stdin = open('input.txt')

L = int(input())
print(L//5 + (1 if L%5 else 0))

