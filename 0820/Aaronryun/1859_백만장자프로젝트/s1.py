import sys

sys.stdin = open('input.txt')

for test in range(1, 1 + int(input())):
    N = int(input())

    data = list(map(int, input().split()))
    data.reverse() # 뒤집어보자
    answer = 0

    target= max(data)
    while data:
        position = data.pop() # 처음에는 pop(0)을 해줬는데 시간초과.... 슬라이싱 써서 풀까 하다가 그냥 뒤집어서 팝했다
        if data and position == target:  # 매번 최댓값을 찾았더니 시간초과가 나서 조건 추가
            target = max(data)

        if target - position >0: # 결과값이 마이너스 인데도 계산하는 경우가 발생해서 조건 추가 생각해보면 위에서 컨티뉴를 써서 밑에 계산을 건너뛰어도 괜찮을듯
           answer += (target - position)

    print('#{} {}'.format(test, answer))
