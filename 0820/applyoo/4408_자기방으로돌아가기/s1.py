import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(T):
    N = int(input())
    arr = []
    rooms = [0] * 201 # 방 개수 200개(홀짝을 고려하기 힘드므로 합쳐줄 것)
    for i in range(N):
        x, y = map(int, input().split())
        x = (x+1)//2 # (1,2) (3,4) ~~~ (399,400)을 짝을 짓기 위해
        y = (y+1)//2
        arr.append((x, y))

    for x, y in arr:
        if x > y: # x가 큰 경우
            x, y = y, x # 스왑
        for i in range(x, y+1): # x~y까지 방에 모두 +1
            rooms[i] += 1

    print('#{} {}'.format(test+1, max(rooms))) # rooms의 최대값이 걸린 시간 단위임