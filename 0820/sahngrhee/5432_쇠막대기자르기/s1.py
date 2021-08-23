import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    iron_bar = input()

    stack = []
    ans = 0

    for i in range(len(iron_bar)):
        #열린괄호면 넣어
        if iron_bar[i] == '(':
            stack.append('(')
        else:
            # 아니라면 뺴
            stack.pop()
            if iron_bar[i-1] =='(':
                #얘는 레이저
                ans += len(stack)
            else:
                ans += 1

    print("#{} {}".format(test_case, ans))
