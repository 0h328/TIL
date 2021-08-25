# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14tDX6AFgCFAYD&categoryId=AV14tDX6AFgCFAYD&categoryType=CODE&problemTitle=1224&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

import sys
sys.stdin = open('input.txt')

for T in range(1, 11):
    input()
    nums = []
    opers = []
    for s in input():
        if s == '(':
            opers.append(s)
        elif s == '+':
            while opers:
                temp = opers.pop()
                if temp == '(':
                    opers.append(temp)
                    break
                elif temp == '+':
                    nums.append(nums.pop() + nums.pop())
                elif temp == '*':
                    nums.append(nums.pop() * nums.pop())
            opers.append(s)
        
        elif s == '*':
            while opers:
                temp = opers.pop()
                if temp in ['(', '+']:
                    opers.append(temp)
                    break
                else:
                    nums.append(nums.pop()*nums.pop())
            opers.append(s)

        elif s == ')':
            while opers:
                temp = opers.pop()
                if temp == '(':
                    break
                elif temp == '+':
                    nums.append(nums.pop()+nums.pop())
                elif temp == '*':
                    nums.append(nums.pop()*nums.pop())
        else:
            nums.append(int(s))

    print('#{} {}'.format(T, nums.pop()))

#1 672676
#2 1974171
#3 12654
#4 38756
#5 4035
#6 155304
#7 6964
#8 2819
#9 24711
#10 208785

