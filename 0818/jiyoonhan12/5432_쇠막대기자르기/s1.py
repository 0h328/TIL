import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    line = input()
    stack = []
    cut = 0

    for i in range(len(line)):
        if line[i] == '(':
            stack.append(line[i])
        else: # )
            if line[i-1] == ')': # 레이저 아닐 때 = 막대 end
                stack.pop()
                cut += 1 # 막대 끝나면 토막 하나 더 나옴
            else: # 레이저 커팅 구간
                stack.pop()
                cut += len(stack) # 지금 있는 막대 길이만큼 cut 추가

    print('#{} {}'.format(t, cut))