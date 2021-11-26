import sys
sys.stdin = open('input.txt')

N = input()
stack = []
for chr in N:
    if chr in ['+','-','*','/']:
        stack.append(chr)
    else:
        print(chr, end = '')

while len(stack)>=1:
    print(stack.pop(), end = '')
