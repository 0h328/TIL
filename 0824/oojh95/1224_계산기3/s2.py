import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    num = list(input())
    isp = {'(':0, '+':1, '*':2}
    stack = []
    result = []
    arr = []
    top = -1
    for i in range(N):  #중위표현식을 후위표현식으로.
        if num[i] == '(':
            stack.append(num[i])
            top = 0
        elif num[i] in isp and top < isp[num[i]]:
            stack.append(num[i])
            top = isp[stack[-1]]
        elif num[i] in isp and top >= isp[num[i]]:
            while top >= isp[num[i]]:
                result.append(stack.pop())
                top = isp[stack[-1]]
            stack.append(num[i])
            top = isp[stack[-1]]
        elif num[i] == ')':
            while True:
                a = stack.pop()
                if a == '(' and stack:
                    top = isp[stack[-1]]
                    break
                elif a == '(':
                    top = -1
                    break
                else:
                    result.append(a)
        else:
            result.append(num[i])

    for i in range(len(result)):    # step2 후위표현식 연산과정
        if result[i] == '+':
            arr.append(arr.pop()+arr.pop())
        elif result[i] == '*':
            arr.append(arr.pop()*arr.pop())
        else:
            arr.append(int(result[i]))
    print('#{} {}'.format(tc, arr.pop()))
