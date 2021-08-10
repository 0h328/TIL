import sys
sys.stdin = open('input.txt')

tc = int(input())
for tc in range(tc):
    bus_info = list(map(int, input().split()))
    gas_station = list(map(int, input().split()))
    bus_step = bus_info[0]
    cnt = 0
    for i in range(1,len(gas_station)) :
        if gas_station[i] - gas_station[i-1] > bus_info[0] :
            print('#{0} {1}'.format(tc+1, cnt))
            break
    else :
        while bus_step < bus_info[1]:
            if bus_step in gas_station:
                cnt += 1
                bus_step += bus_info[0]
            else :
                bus_step = bus_step - 1
        print('#{0} {1}'.format(tc+1, cnt))


