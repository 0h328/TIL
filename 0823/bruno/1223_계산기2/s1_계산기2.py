import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    my_string = input()
    back = ''    # 후위표기법 수식
    stack = []   # 연산자가 저장될 스택

    for strs in my_string:
        if strs == '*':
            stack.append(strs)
        elif strs == '+':
            while stack:    # +보다 낮은 연산자는 없으므로 빌 때까지 pop
                back += stack.pop()
            stack.append(strs)
        else:               # 숫자는 back에 저장
            back += strs

    while stack:            # 모든 연산자를 뒤에 갖다 붙이기
        back += stack.pop()
    print(back)
    result = []
    for strs2 in back:

        if strs2 == '+':
            b = result.pop()
            a = result.pop()
            c = int(a) + int(b)
            result.append(c)
        elif strs2 == '*':
            b = result.pop()
            a = result.pop()
            c = int(a) * int(b)
            result.append(c)
        else:
            result.append(int(strs2))

    print('#{} {}'.format(tc, result[0]))