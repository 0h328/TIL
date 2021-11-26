# 장훈님 풀이
import sys
sys.stdin = open('input.txt')

def bubblesort(height_state):   #버블정렬함수
    for i in range(99, 0, -1):
        for j in range(i):
            if height_state[j] > height_state[j + 1]:
                height_state[j], height_state[j + 1] = height_state[j + 1], height_state[j]


def dumpfunc(dump, height_state):   #더미 작동함수 가장 최대최소값의 블럭을 옮긴후 재귀함수로 dumfunc를 불러온다.
        if dump == 0:
            return height_state[99] - height_state[0]
        else:
            height_state[0] += 1
            height_state[99] -= 1
            bubblesort(height_state)
            return dumpfunc(dump-1, height_state)

T = 10  #테스트케이스
for test_case in range(1, T + 1):
    dump = int(input()) #덤프횟수
    height_state = list(map(int, input().split()))  #초기 높이 정보(가로는 100)
    bubblesort(height_state)

    print('#{} {}'.format(test_case, dumpfunc(dump, height_state)))


