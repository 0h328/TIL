import sys, math
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if dist == 0 and r1 == r2:  # 두 원이 동심원이고, 반지름이 같을 때
        print(-1)
    elif abs(r1-r2) < dist < r1+r2: # 두 원이 서로 다른 두 점에서 만날 때
        print(2)
    elif abs(r1-r2) == dist or r1 + r2 == dist: # 내접이거나 외접인 경우
        print(1)
    else:
        print(0)