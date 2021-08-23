import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    stack = []
    result = 0
    temp = input()
    for i, s in enumerate(temp):
        if s == '(':
            stack.append(s)
        elif temp[i-1]== '(':
            stack.pop()
            result+=len(stack)
        else:
            stack.pop()
            result+=1
            
    print('#{} {}'.format((T+1), result))

#1 17
#2 24