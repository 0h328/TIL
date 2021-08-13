import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = input()

    pair = []
    ans = 0

    # data 최대 길이가 10만이므로 반복문 한바퀴 내에 끝내야 한다.
    for i in range(len(data)):
        # ( 는 pair에 넣음
        if data[i] == '(':
            pair.append(data[i])
        # 레이저의 경우, 짝 맞는 ( 하나 빼주고, 나머지 (는 레이저에 의해 잘리면서 그 갯수만큼 +1씩 된다
        elif i > 0 and data[i] == ')' and data[i-1] == '(':
            pair.pop()
            ans += len(pair)
        # 막대의 끝인 경우, 잘리고 남은 부분인 하나만큼만 더해주면 된다
        else:
            pair.pop()
            ans += 1

    print('#{} {}'.format(tc, ans))