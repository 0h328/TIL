import sys
sys.stdin = open('input.txt')

for T in range(1, 11):
    N = input()
    exp = input()

    opers = []
    nums = []

    # 연산자
    # stack에 연산자가 있고, 현재 연산자보다 pop한 연산자 우선순위가 같거나 높을 경우 연산후 저장
    # 아닐 경우 push
    
    # 숫자
    # push

    # 괄호의 경우, )일 경우 연산자 pop해서 (를 만날때까지 연산

    for s in exp:
        if s == '+':
            if len(opers):
                while opers:
                    a = nums.pop()
                    b = nums.pop()
                    if opers.pop() == '+':
                        nums.append(a+b)
                    else:
                        nums.append(a*b)
            opers.append(s)

        elif s == '*':
            if len(opers):
                while opers:
                    if opers.pop() == '+':
                        opers.append('+')
                        break
                    a = nums.pop()
                    b = nums.pop()
                    nums.append(a*b)
            opers.append('*')

        else:
            nums.append(int(s))

    else:
        while opers:
            a = nums.pop()
            b = nums.pop()
            if opers.pop() == '+':
                nums.append(a+b)
            else:
                nums.append(a*b)

    print('#{} {}'.format(T, nums.pop()))

#1 28134
#2 195767
#3 4293
#4 1592
#5 477326
#6 45647
#7 102951
#8 6548
#9 1394
#10 4285
