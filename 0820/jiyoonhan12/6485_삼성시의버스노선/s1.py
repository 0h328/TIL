import sys
sys.stdin = open('input.txt')

# runtime error
T = int(input())

for t in range(1, T+1):
    N = int(input())
    station = [0] * 5001
    for n in range(N):
        start, end = map(int, input().split())
        for i in range(start, end+1):
            station[i] += 1
    print(station)
    #cnt = []
    print('#{}'.format(t), end='')
    P = int(input())
    for p in range(1, P+1):
        #cnt.append(station[int(input())])
        print(' {}'.format(station[p]), end='')
    #print('#{}'.format(t))
    print()