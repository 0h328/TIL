# 제 코드 아니고 구글 검색해서 참고하고 한번 돌려본 코드입니당..!

import sys
sys.stdin = open('input.txt')

def comb(cnt, idx, start):  # 조합 찾기
    # 현재 선택한 개수, p1의 값을 바꿔 줄 위치 값, 시작점
    if cnt == (N//2):  # 현재 선택한 개수가 찾으려는 숫자와 같은 경우
        cal(0)
        return

    else:
        for q in range(start, N):
            person1[idx] = q
            comb(cnt + 1, idx + 1, q + 1)  # 선택한 개수 + 1, 위치 + 1, 시작점은 현재 값 + 1
    return

def cal(p2_cnt):  # 계산
    global result
    customer1 = 0  # 고객 1의 합
    customer2 = 0  # 고객 2의 합

    for w in range(N):  # 고객 2의 재료 선택
        if w not in person1:
            person2[p2_cnt] = w
            p2_cnt += 1

    for i in range(N // 2):  # 계산하기, 홀수가 존재하기 때문에 하나씩 뽑아서 대조하면서 계산
        # if n == 6이면 n//2 == 3이고, 두개씩 짝 지으면 한 개가 남아버림

        for j in range(N // 2):
            if i != j:  # 같은 값 제외 [1, 2]에서 1+1 같은 경우 배제하기 위함
                customer1 += foods[person1[i]][person1[j]]
                customer2 += foods[person1[i]][person2[j]]

    if abs(customer1 - customer2) < result:  # min_res보다 작으면 값 바꾸기
        result = abs(customer1 - customer2)

    return
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    foods = [list(map(int, input().split())) for _ in range(N)]
    # print(food)
    # [[0, 5, 3, 8],
    #  [4, 0, 4, 1],
    #  [2, 5, 0, 3],
    #  [7, 2, 3, 0]]
    result = 9999999999
    person1 = [0] * (N // 2)
    person2 = [0] * (N // 2)
    comb(0, 0, 0)
    # print(visited)
    print('#{} {}'.format(tc, result))