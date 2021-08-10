import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    first = list(map(int,input().split()))
    second = list(map(int,input().split()))
    K = first[0]
    N = first[1]
    M = first[2]
    position = 0  #현재 버스의 위치
    cnt = 0 # 충전 횟수
    station = [0] * (N+1) # 역의 list

    for b in second:
        station[b] += 1 # 충전기가 설치된곳을 1로 변경

    for F in range(N+1): # < 몇번 돌리냐는 의미없음 최대치인 N+1으로 가정(충전기가1로 되있을수도있으니)
        K = first[0] # 돌릴때마다 충전기의 거리를 초기화
        while K > 0: # while문을 돌리는데, 충전소를 만나면 break로나가고, list범위값(도착)을 나가도 break
                     # 그리고 만약 자연스럽게 K==0이 되게되면 while문 종료시 cnt를 0으로 초기화하고 뒤에 조건문
            if (position + K) >= N:
                break
            else:
                if station[position + K] == 1:
                    position = position + K
                    cnt += 1
                    break
                else:
                    K -= 1
                    if K == 0:
                        cnt = 0
        if (position + K) >= N: # < 만약 기준선이상이거나 도착했다면, 위에서 돌린 for문을 중지하고 출력
            print('#{} {}'.format(i + 1, cnt))
            break
        elif cnt == 0: # < cnt가 0이되어 초기화되었다는것은 충전소를 만나지 못했다는것이기 떄문에 0을 출력하고 break
            print('#{} {}'.format(i + 1, cnt))
            break

