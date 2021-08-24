import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    iron_stick = input()
    l = len(iron_stick)
    lazer = 0
    stick = 0
    cnt = 0       # 쇠막대기 조각의 총 개수

    for i in range(l):
        if iron_stick[i] == '(':
            if iron_stick[i+1] == ')':        # '()' 이므로 레이저 생성
                lazer = 1
            else:                             # '((' 인 경우 막대기 한 개씩 생김
                stick += 1
        else:
            if lazer == 1:                    # ')'이고 레이저가 1개인 경우 레이저에 의해 막대기가 잘려짐
                cnt += stick                  # 쇠막대기 조각의 개수에 막대기 개수 더해줌
                lazer = 0                     # 이후 레이저는 0으로 초기화
            else:                             # ')'이고 레이저도 0인 경우
                cnt += 1                      # '))'와 같은 경우이므로 조각이 하나 나오기 때문에 조각에 하나 더해줌
                stick -= 1                    # 쇠막대기 개수를 하나 줄여줌
    print('#{} {}'.format(tc, cnt))



"""
#1 17
#2 24
"""