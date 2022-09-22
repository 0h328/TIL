import sys
sys.stdin = open('input.txt')

W, H, X, Y, P = map(int, sys.stdin.readline().split())
cnt = 0
for _ in range(P):
    x, y = map(int, sys.stdin.readline().split())

    # 가운데 직사각형 내부에 있는 경우(둘레 포함)
    if (X <= x <= X + W) and (Y <= y <= Y + H):
        cnt += 1
        continue

    # 왼쪽 반원, 오른쪽 반원 내부에 있는 경우(둘레 포함)
    R = H / 2
    d1 = ((x - X) ** 2 + (y - (Y + R)) ** 2) ** 0.5
    d2 = ((x - (X + W)) ** 2 + (y - (Y + R)) ** 2) ** 0.5
    if d1 <= R or d2 <= R:
        cnt += 1

print(cnt)