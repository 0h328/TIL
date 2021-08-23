import sys
sys.stdin = open('input.txt')

t = int(input())
for num in range(1,t+1):
    s = input()
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    print('#{} {}'.format(num,len(stack)))
