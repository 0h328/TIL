import sys
sys.stdin = open('input.txt')

T = int(input())


for case in range(T):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    pos = [[i+1,cheese[i]] for i in range(M)]
    fire = [[-1, -1] for _ in range(N)]
    res = []
    point = 0
    while True:
        if fire == [[0, 0] for _ in range(N)]:
            break
        if point == N:
            point = 0
        if fire[point][1] == -1:
            if pos:
                fire[point] = pos.pop(0)
                fire[point][1] //= 2
            else:
                fire[point] = [0, 0]
            point += 1
            continue
        elif fire[point][1] == 0:
            if fire[point][0] != 0:
                res.append(fire[point][0])
            if pos:
                fire[point] = pos.pop(0)
                fire[point][1] //= 2
            else:
                fire[point] = [0, 0]
            point += 1
            continue
        elif fire[point][1] > 0:
            fire[point][1] //= 2
            point += 1
            continue
    print('#{} {}'.format(case +1 ,res[-1]))



