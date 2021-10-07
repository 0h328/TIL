'''
24시간 운영되는 물류센터에는 화물을 싣고 내리는 도크가 설치되어 있다.
0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록
최대 몇 대의 화물차가 이용할 수 있는지 알아내

신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시
앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.
예를 들어 앞 작업의 종료 시간이 5시면 다음 작업의 시작 시간은 5시부터 가능
'''

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    time_list = []      # (시작, 종료) 시간을 담을 리스트
    stack = []          # 해당하는 친구만 옮길려고

    for _ in range(N):
        (s, e) = map(int, input().split())
        time_list.append((e, s))    # 종료시간을 기준으로 정렬할거라서 거꾸로 넣음
        time_list.sort()            # 종료시간 기준으로 오름차순 정렬

    stack.append(time_list.pop(0))  # 첫 시간만 넣어주고, 가장 빨리 끝나니까
    # print(stack)
    # print(time_list)

    for i in time_list:             # 이제 첫 종료시간이랑 나중에의 시작시간이 안 겹치는 애들만 stack에 넣어줌
        if stack[-1][0] <= i[1]:
            stack.append(i)

    print('#{} {}'.format(tc, len(stack)))      # 해당 갯수가 답!