import sys
sys.stdin = open('input.txt')

# thought process: 2분
# enQueue, deQueue, front 와 rear 이용해보자
# mod 이용해서 원형 큐 구현
# 소요시간: 30분

# 궁금증: front 를 10번 움직이는거랑 수열 자체를 10번 움직이는거랑 왜 차이가 있을까
def move():
    global rear
    global front
    if rear == 0:
        rear = N-1
    else:
        rear -= 1
    if front == 0:
        front = N-1
    else:
        front -= 1

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())        # 수열의 길이, 이동 횟수 인풋값
    Q = list(map(int, input().split()))     # 큐 생성
    front = 0
    rear = N - 1
    while M:                                # 남은 이동횟수가 0이 될 때까지 루프
        move()
        M -= 1
    print('#{} {}'.format(tc, Q[front]))