import sys                                              # input 데이터를 불러온다.
sys.stdin = open('input.txt')

T = int(input())                                        # 테스트 케이스를 받아온다.
for t in range(T):                                      # 테스트 케이스에 맞는 k:이동거리, n:도착지점, m: 주유소 수를 받아온다.
    k, n, m = list(map(int, input().split()))
    numbers = list(map(int, input().split()))           # 'numbers'변수를 통해 주유소 위치를 받아온다.

    oil = [0] * n                                       # 'oil' 주유소 위치 리스트를 생성한다. 충전하는 장소
    station = [0] * n                                   # 'station' 머무른 주유소 리시트를 생성한다. 충전한 장소,멈춘곳
                                                        # 리스트 -> 수로 count 해주는 식으로
    for i in range(m):
        oil[numbers[i]] += 1                            # 'oil' 주유소 위치 리스트에 'numbers'를 통해 주유소가 존재하는 경우 1로 지정한다.
    here, move = k, k                                   # 현재 위치를 이동거리 k만큼 이동한 거리라고 지정한다. # 이동거리변수를 k로 지정한다.

    while True:
        if here >= n:                                   # 현재의 위치가 도착지점보다 큰경우 머무른 'station'을 더해준다.
            result = sum(station)
            break
        elif oil[here] == 0:                            # 이외에, 현재의 주유소의 정보가 0 인경우 = 주유소 없음
            here -= 1                                   # 현재 위치와 이동 위치를 -1
            move -= 1
            if move == 0:                               # 이동 위치가 0인 경우 주유를 할 수 없는 상황이기에 'result'0의 값을 출력한다.
                result = 0
                break
        elif oil[here] == 1:                            # 이외에, 현재 위치와 이동 위치를 변경한 경우 현재의 위치의 주유 정보가 1인 경우
            move = k                                    # 주유소가 없는 경우 무조건 3칸(k)을 움직인다고 생각.
            station[here] = 1                           # 현재 위치를 머무른 주유소로 지정하여 1의 값을 넣어준다.
            here += k                                   # 이후, 이동 k 만큼 현재 위치를 옮겨준다.
    print('#{} {}'.format(t+1, result))