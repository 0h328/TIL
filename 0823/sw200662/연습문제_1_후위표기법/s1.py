import sys
sys.stdin = open('input.txt')

my_string = input()
stack = []

for i in range(len(my_string)):
    if my_string[i] == '+' or my_string[i] == '-' or my_string[i] == '*' or my_string[i] == '/':
        stack.append(my_string[i])
    else:
        print(my_string[i],end='')
while stack:
    print(stack.pop(),end='')