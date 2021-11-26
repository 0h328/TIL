import sys
sys.stdin = open('input.txt')

my_str = input()
stack = []
ans = []
k = ['+', '-', '*', '/']

for i in range(len(my_str)):
    if my_str[i] in k:
        stack.append(my_str[i])
    else:
        print(my_str[i], end='')

while stack:
    print(stack.pop(), end='')


