import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    s1 = []
    s2 = []
    N = int(input())
    data = input()
    # 1. 중위표현식 -> 후위표현식
    for c in data:              # 계산식에서 하나씩 값을 가져오면서
        if '0' <= c <= '9':     # 숫자면 stack에 추가
            s1.append(c)
        else:                   # 연산자면
            if c == '+':        # + 연산자면 (*보다 우선순위가 낮음)
                while len(s2) != 0:     # stack2가 비워지기 전까지
                    s1.append(s2.pop()) # stack2에서 계속 pop을해서 stack1에 옮기고
                s2.append(c)            # stack2가 다 비워졌다면 해당 연산자를 stack2에 추가하고
            else:                       # * 연산자면
                s2.append(c)            # 바로 stack2에 추가한다. (+보다 우선순위 위)

    while len(s2) != 0:     # stack2가 비워질 때까지
        s1.append(s2.pop()) # s2에서 pop을하고 그걸 stack1으로 옮긴다.

    # 2. 후위표현식으로 변환된 요소를 실제 계산
    for c in s1:              # stack1에서 값을 꺼내
        if '0' <= c <= '9':   # 숫자라면
            s2.append(int(c)) # 형변환을 해서 stack2에 넣고
        else:                 # 연산자면
            opr1 = s2.pop()   # s2에서 값을 꺼내고 (2개의 숫자를 연산해야 하기 때문에 2개)
            opr2 = s2.pop()
            if c == '+':               # c가 +면
                s2.append(opr1 + opr2) # 더해서 넣고
            else:                      # *면
                s2.append(opr1 * opr2) # 곱해서 넣자

    ans = s2.pop()
    print('#{} {}'.format(tc, ans))