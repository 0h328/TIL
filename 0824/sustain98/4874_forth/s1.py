import sys
sys.stdin = open('input.txt')

t = int(input())

for idx in range(1, t+1):
    s = list(input().split())
    stack = []
    try:
        for i in s:
            if i.isdigit():
                stack.append(int(i))
            elif i == '.' and len(stack) > 1:           # 중간에 .이 오는 경우 error -> (수정) .이 왔을때 그 앞의 값들이 온전히 계산을 마치지 못한경우
                res = 'error'
                break
            elif i == '.':
                res = stack.pop()
                break
            else:
                # 여기에서 stack길이가 2이상인지 확인해도 될듯
                a = stack.pop()
                b = stack.pop()
                if i == '*':
                    stack.append(b*a)
                elif i == '/':
                    stack.append(int(b/a))
                elif i == '+':
                    stack.append(b+a)
                else:
                    stack.append(b-a)
    except:
        res = 'error'
    print('#{} {}'.format(idx, res))

