import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1,t+1):
    k, n, m = map(int, input().split())
    charge = list(sorted(map(int, input().split()))) + [n]  #정렬되서 주어진다는 조건이 없었으므로 sorted, 맨끝에 [n]은 아래 for문에서 index에러를 막기 위함
    loc = k                                                 #loc은 현재 상태에서 갈수 있는 최대 거리
    cnt = 0

    for i in range(m):
        if charge[i] <= loc < charge[i+1]:                  #지금 i가 가리키는 충전소가 내가 갈수있는한 최대로 먼 충전소여야하므로 다음 조건 사용
            cnt += 1
            loc = charge[i] + k                             #충전후 갈 수 있는 최대 위치
        elif loc < charge[i]:                               #더이상 나아갈 수 없는 경우 break
            cnt = 0
            break
        else: 
            continue

        if loc >= n:
            break

    print('#{} {}'.format(idx, cnt))




#3
#0
#4
