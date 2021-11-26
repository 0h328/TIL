import sys
sys.stdin = open('input.txt')

def count_stick(x):                     # 막대기 개수를 세서 반환할 함수를 정의
    stack = []                          # 빈 스택 생성
    ans = 0
    for i in range(len(x)):             # 막대 데이터에 대해서 앞에서부터 순회
        if x[i] == "(":                 # 막대의 왼쪽 '('이 나타나면 스택에 push
            stack.append("(")           
        elif x[i] == ")":               # 막대의 오른쪽 ')이 나타나면,
            stack.pop()                 # 스택의 마지막 값을 제거해주고
            if x[i - 1] == "(":         # 1. 이전 위치가 '('이면 레이저 포인터가 등장했다는 뜻
                ans += len(stack)       # 지금까지 스택에 들어가있는 막대의 왼쪽 부분의 개수만큼으로 막대가 쪼개짐
            elif x[i - 1] ==")":        # 2. 만약 이전 위치가 ')'라면 
                ans += 1                # 레이저 포인터는 아니지만 막대 하나가 끝난다는 뜻이므로,
                                        # 잘려나간 마지막 막대 끝부분인 1개를 더해줌
    return(ans)

T = int(input())

for tc in range(1, T + 1):
    data = input()
    print('#{}'.format(tc), end=' ')
    print(count_stick(data))