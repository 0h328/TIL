'''
2차원 배열을 한번씩 순회하면서 1은 n 극이므로 다음 행으로
2는 s극이므로 이전 행으로 이동 (조건에 옮길 좌표의 값이 0 일때만)
만약 이동하는게 범위를 벗어나게되면 현재 위치의 좌표 값을 0 으로

2중 반복문을 더이상 옮길수 없을때까지 반복? -> 너무 많은 반복으로 시간복잡도 증가
한번 값을 확인했을때 아래/위 의 행을 확인하여 교착 여부 판단 (자성체들 위치 정보 필요없음)

교착상태 개수 판단 - 스택으로 판단 (11112222211112222 -> 스택 내부에 같은 숫자면 쌓지 않고, 다른 숫자일경우만 추가하여 최종 갯수 구하고 2로 나누기)

----- 위의 내용 구현의 어려움, 조건이 너무 많음
스택으로 사용하여 구함
짝수 인덱스에는 1이 들어와야하고 홀수 인덱스에는 2가 들어와야 함
인덱스 관리를 잘하자......
'''

import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    M = int(input())                # size of table
    board = [list(map(int, input().split())) for _ in range(M)]     # 1 - N / 2 - S / table top - N / table bottom - S
    answer = 0

    for i in range(M):
        stack = []
        for j in range(M):
            if board[j][i] == 1:
                if not stack:           # 비어 있으면 1추가
                    stack.append(1)
                elif stack[-1] == 2:    # 비어 있지 않고, 마지막이 2라면 추가
                    stack.append(1)

            elif board[j][i] == 2:
                if stack and stack[-1] == 1:    # 비어있지 않고 마지막이 1이면 2 추가
                    stack.append(2)

        answer += len(stack)//2
    print('#{} {}'.format(tc, answer))