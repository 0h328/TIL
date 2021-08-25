import sys
sys.stdin = open('input.txt')

# thought process: 8분
# 각 1차원 리스트
# 큐에 넣고 맨앞 빼고 -1 해서 다시 큐에 삽입
# 무한 반복, until 큐의 맨 뒤값이 0, 이때
# 맨 앞 값을 리스트에 저장, 다음 1차원 리스트에서도 반복

# 풀이: 1시간 27분 47초 소요...

# 힘들었던점: 문제 자체가 너무 헷갈렸다
# 보기쉽게 4자리로 쪼개져 있을뿐, 전체 인풋값들을 돌려가며 암호를 찾거나,
# 2차원 배열을 만들어서, 각 4자리수 마다 암호를 찾아서, 맨 앞의 값들을 합친 값을 찾거나,
# 2차원과 1차원 배열상에서 동시에 자리를 바꾸어가며 암호를 찾는 줄 알고 다 시도해보며
# 하루종일 고통받다가 하루가 다 가버린 웃픈 하루 ^^
for tc in range(1, 11):
    N = int(input())

    nums = list(map(int, input().split()))
    ans = []            # 정답 리스트 생성
    Q = []              # 큐 생성
    front = 0
    rear = -1

    for num in nums:    # 큐에 숫자들 입력
        Q.append(num)

    i = 1                           # 이동 할때마다 증가하는 이동 값 초기화
    while Q[rear] > 0:
        temp = Q.pop(front) - i     # deQueue, 인큐하기위해 pop 된 값에 i 더함
        Q.append(temp)              # enQueue
        if i == 5:                  # i 가 5에 도달하면 1로 초기화
            i = 1
        else:                       # 아니면 1씩 증가
            i += 1
    if Q[rear] < 0:                 # 암호 마지막 자리가 0 이하면
        Q[rear] = 0                 # 0 으로 수정

    print('#{}'.format(tc), end=' ')        # 리스트 unpack 어떻게하더라..
    for i in Q:
        print(i, end=' ')
    print()




