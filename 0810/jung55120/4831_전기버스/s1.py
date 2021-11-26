import sys
sys.stdin = open('input.txt')

tc = int(input())
for tc in range(tc):                                        # 테스트 케이스만큼 반복
    bus_info = list(map(int, input().split()))              # 버스 정보를 bus_info 리스트에 저장
    gas_station = list(map(int, input().split()))           # 정류소 정보를 gas_station 리스트에 저장
    bus_step = bus_info[0]                                  # 버스가 처음 가는 간격을 bus_step에 저장
    cnt = 0                                                 # 충전하는 횟수를 cnt에 저장해주기 위해서 0 저장
    for i in range(1,len(gas_station)):                     # 먼저, gas_station의 위치를 체크
        if gas_station[i] - gas_station[i-1] > bus_info[0]: # 만약, gas_station의 간격이 버스가 한번에 갈 수 있는 간격보다 클 때
            print('#{0} {1}'.format(tc+1, cnt))             # 프린트 0 하고 바로 break
            break
    else:                                                   # for 문이 제대로 돌지 못하면
        while bus_step < bus_info[1]:                       # bus_step이 종점보다 커질 때까지 반복
            if bus_step in gas_station:                     # bus_step이 gas_station 리스트 안에 들어있으면
                cnt += 1                                    # cnt에 1을 추가
                bus_step += bus_info[0]                     # bus_step에 버스가 한 번 충전 후 갈 수 있는 거리를 더해줌
            else:                                           # if에서 true가 아니면(bus_step이 gas_station 리스트 안에 없으면)
                bus_step = bus_step - 1                     # bus_step을 1만큼 작게 해서(뒤로 돌아가서) gas_station 내의 숫자에 닿도록...
        print('#{0} {1}'.format(tc+1, cnt))                 # cnt를 출력(tc가 0부터 시작이라 1 더해줌)


