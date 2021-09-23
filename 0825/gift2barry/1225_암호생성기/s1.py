import sys
sys.stdin = open('input.txt')

# thought process: 8분
# 각 1차원 리스트
# 큐에 넣고 맨앞 빼고 -1 해서 다시 큐에 삽입
# 무한 반복, until 큐의 맨 뒤값이 0, 이때
# 맨 앞 값을 리스트에 저장, 다음 1차원 리스트에서도 반복

# 소요: 1시간 27분 47초

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
        # if i == 5:                # i 가 5에 도달하면 1로 초기화
        #     i = 1
        # else:                     # 아니면 1씩 증가
        #     i += 1
        i %= 5                      # 정현님 idea (i = i % 5)  위에 내 코드랑 동일한 뜻
        i += 1
    if Q[rear] < 0:                 # 암호 마지막 자리가 0 이하면
        Q[rear] = 0                 # 0 으로 수정

    print('#{} {}'.format(tc, ' '.join(map(str, Q))))
    # print(*Q)                     # 이거 쓸때는 .format 쓰면 ㄴㄴ
    # for i in Q:                   # 리스트 unpack 어떻게하더라..
    #     print(i, end=' ')
    # print()
    # ' '.join(map(str, Q))





