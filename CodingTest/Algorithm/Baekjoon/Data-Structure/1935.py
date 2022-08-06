import sys
sys.stdin = open('input.txt')

N = int(input())
word = input()

nums = [0]*N			        # 피연산자값을 저장하기 위한 nums 생성
for i in range(N):
    nums[i] = int(input())      # 피연산자값 받기

stack = []                      # stack 리스트를 통해 후위표기식 계산
for i in word:
    if 'A' <= i <= 'Z':		                    # word를 돌면서 알파벳이면
        stack.append(nums[ord(i)-ord('A')])  # stack에 저장
    else :						                # 연산자면
        str_2 = stack.pop()		                # stack 리스트의 마지막 2항목을 꺼내와서 계산한다.
        str_1 = stack.pop()

        if i =='+':
            stack.append(str_1+str_2)
        elif i == '-':
            stack.append(str_1-str_2)
        elif i == '*':
            stack.append(str_1*str_2)
        elif i == '/':
            stack.append(str_1/str_2)

print('%.2f' %stack[0])