import sys

sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N = int(input())
    list_bus = []
    list_station = []
    for k in range(N):
        A, B = map(int, input().split())
        list_bus.append([A, B])
    P = int(input())
    for c in range(P):
        list_station.append(int(input()))
    all_list = [0] * (5001)
    for z in list_bus:
        while z[0] <= z[1]:
            all_list[z[0]] += 1
            z[0] += 1
    print('#{}'.format(i + 1), end=' ')
    for m in list_station:
        print(all_list[m], end=' ')
    print()
