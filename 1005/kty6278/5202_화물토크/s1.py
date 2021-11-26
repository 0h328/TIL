import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n = int(input())
    car = [list(map(int,input().split())) for _ in range(n)]

    car.sort(key=lambda x:(x[1], x[0]))
    cnt = 1

    start = 0
    for j in range(start, len(car)):
        if car[start][1] <= car[j][0]:
            cnt += 1
            start = j
    print('#{} {}'.format(tc+1, cnt))