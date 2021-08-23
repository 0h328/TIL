import sys
sys.stdin = open('input.txt')

for tc in range(1):
    N = int(input())
    my_string = input()
    back = ''    # 피연산자 및 낮은 우선순위 연산자
    stack = []   # 높은 우선순위 연산자
    priority = {'+' : 1, '*' : 2}
    for strs in my_string:
        if len(stack) == 0 or strs == '*':
            stack.append(strs)
        elif strs == '+':
            while stack:
                back += stack.pop()
            stack.append(strs)
        else:
            back += strs
    print(back)
    break

    while stack:
        for oper in stack:
            b = nums.pop()
            a = nums.pop()
            if oper == '+':
                c = int(a) + int(b)
            elif oper == '*':
                c = int(a) * int(b)
            nums.append(c)
        print(nums)
        # 아직 푸는중입니다..