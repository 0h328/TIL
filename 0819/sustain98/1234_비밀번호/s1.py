import sys
sys.stdin = open('input.txt')

for num in range(1,11):
    n, s = input().split()
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    print('#{} {}'.format(num, ''.join(stack)))
