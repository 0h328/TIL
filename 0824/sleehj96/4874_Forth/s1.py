import sys
sys.stdin = open('input.txt')


T = int(input())
tc = 1
while tc <= T:
    data = input().split()

    stack = []

    for letter in data:

        try:                                # 에러처리
            if letter.isnumeric():          # 숫자면
                stack.append(int(letter))   # 스택에 push

            else:                           # 연산자면
                if letter == '.':           # . 이면
                    if len(stack) > 1:      # 스택에 1개 남아있는지 확인
                        ans = 'error'       # 아니면 error -> 채점 시 마지막 10번째 케이스
                    else:                   # 1개 남아있으면
                        ans = stack.pop()   # ans에 저장

                else:                       # . 이 아니면
                    n2 = stack.pop()        # n2 pop
                    n1 = stack.pop()        # n1 pop

                    if letter == '+':
                        stack.append(n1+n2)
                    elif letter == '*':
                        stack.append(n1*n2)
                    elif letter == '-':
                        stack.append(n1-n2)
                    elif letter == '/':
                        stack.append(n1//n2)
        except:             # 숫자를 2개 뽑아야 하는데 스택에 없거나.. 등등
            ans = 'error'

    print('#{0} {1}'.format(tc, ans))
    # break
    tc += 1

