import sys
sys.stdin = open("input.txt")

def count_pieces(data):
    stack = []
    cnt = 0                            # 쇠막대기 조각 개수
    for i in range(len(data)):
        if data[i] == '(':
            stack.append(data[i])
        elif data[i] == ')':
            if data[i-1] == '(':       # 레이저 o => 스택에 들어가 있는 막대기 개수('('의 개수)만큼 더해줌 (그만큼 쪼개졌기 때문에)
                stack.pop()
                cnt += len(stack)
            elif data[i-1] == ')':     # 쇠막대기 하나가 끝나므로 => 끝 조각 하나 더해줌
                stack.pop()
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    data = input()
    print('#{}'.format(tc), end=' ')
    print(count_pieces(data))


# ()(((()())(())()))(())