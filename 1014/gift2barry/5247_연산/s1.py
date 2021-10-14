import sys
sys.stdin = open('input.txt')


'''
총 소요시간 1시간 36분
thought process: 15분
이거 BFS 각이다 (최소 깊이까지 가면 되니까)
목적지는 주어진 자연수 M
리스트에 연산 네개 다 넣고
큐스택에 넣어가며 연산
다만, front, rear 활용해서 작성해보자
정답 나오면 바로 끝, 그게 최소 깊이

질문: 어떻게 연산자 집어넣을까
answer => 그냥 0 = +1,  /  1 = -1  /  2 = *2  /  3 = -10 으로 조건문을 만들자

질문: 깊이는 어떻게 memorize 할까
answer => 4 ** cnt 만큼 방문을 하면 깊이 하나씩 올려주기

질문: 정답 확인 된 깊이 계산
answer => 다른 분들은 visited 활용.. 음 더 생각해보자

'''


def deQueue():
    global Q, front
    if Q:
        front += 1
        return Q[front]
    return

def enQueue(nn):
    global Q, rear, gg
    if nn == M:
        gg = True
    else:
        rear += 1
        Q[rear] = nn
    return

def finder(n):
    global ans, Q
    global front, rear
    enQueue(n)
    while Q and not gg:
        num = deQueue()
        for i in range(4):
            if i == 0:
                new_num = num + 1
            elif i == 1:
                new_num = num - 1
            elif i == 2:
                new_num = num * 2
            else:
                new_num = num - 10
            enQueue(new_num)
    return

int(input())+1
for tc in range(1, 2):
    N, M = map(int, input().split())
    ans = 0
    front, rear = -1, -1
    Q = [0] * 100
    gg = False
    finder(N)


