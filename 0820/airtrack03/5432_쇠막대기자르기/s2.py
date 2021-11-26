import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = input()

    pair = []
    raser = []
    stick_start = []
    stick_end = []
    # 첫 시도 제한시간 초과 => 시작, 끝, 레이저 리스트 순회하면서 데이터 커지면 시간 초과
    for i in range(len(data)):
        # 레이저 위치 append
        if i > 0 and data[i] == ')' and data[i-1] == '(':
            raser.append(i-1)
        # ( 는 pair에 넣고, 바로 다음이 )면 레이저, 아니면 막대 시작점
        if data[i] == '(':
            pair.append(data[i])
            if data[i+1] != ')':
                stick_start.append(i)

        # 괄호 짝 맞으면 ( 하나 빼내줌
        if data[i] == ')' and pair[-1] == '(':
            pair.pop()
            # 바로 전이 ( 가 아니면 막대 끝점
            if i > 0 and data[i-1] != '(':
                stick_end.append(i)

    ans = len(stick_start)
    for i in range(len(stick_start)):
        for r in raser:
            # 레이저가 막대 범위 안이면 잘리면서 개수 1개씩 증가
            if stick_start[i] < r < stick_end[i]:
                ans += 1
            # 레이저가 막대 끝보다 커지면 내부 반복 종료
            elif r > stick_end[i]:
                break

    print('#{} {}'.format(tc, ans))