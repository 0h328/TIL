# 리스트를 90도 회전시켜주는 함수
# in_list : 사용자에게 입력 받은 리스트 / angle : 회전할 각도 (초기 설정 0 / 0: 90도 1: 180도 2: 270도)
import sys
sys.stdin = open('input.txt')



def list_lotation(in_list, angle=0):
    global number

    for i in range(number):
        for j in range(number):
            # 90도를 회전하면 값이 저장되는 위치 : 마지막 column 에서 고정, 첫번째 row 에서 1씩 증가
            answer[angle][j][-1-i] = in_list[i][j]

    if angle != 2:
        list_lotation(answer[angle], angle+1)


testCase = int(input())

for index in range(1, testCase+1):
    number = int(input())

    # 배열 입력받아서 2차원 리스트 변수에 저장
    in_list = []
    for _ in range(number):
        in_list.append(list(map(int, input().split())))

    # 정답을 저장할 3차원 리스트 변수
    # answer[0] - 90도, answer[1] - 180도, answer[2] - 270도
    answer = [[[0]*number for _ in range(number)] for _ in range(3)]

    # 90도 회전시키는 재귀함수 호출
    list_lotation(in_list)

    print(f'#{index}')
    for b in range(number):
        for a in range(3):
            for c in range(number):
                print(answer[a][b][c], end='')
            print(' ', end='')
        print()