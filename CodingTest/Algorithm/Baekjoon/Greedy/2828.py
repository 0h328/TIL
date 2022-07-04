import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
j = int(input())

apple = []

for _ in range(j):
    apple.append(int(input()))

move = 0

end = M     # 바구니의 오른쪽 끝 위치를 저장
start = 1   # 바구니의 왼쪽 끝 위치를 저장

for i in range(j):
    # 바구니가 사과를 받을 수 있는 위치인 경우
    if (end >= apple[i] and start <= apple[i]):
        continue
    # 사과가 바구니의 오른쪽에서 떨어지는 경우
    elif (end < apple[i]):
        move += apple[i] - end
        end = apple[i]
        start = apple[i] - (M-1)
    # 사과가 바구니의 왼쪽에서 떨어지는 경우
    elif (start > apple[i]):
        move += start - apple[i]
        start = apple[i]
        end = apple[i] + (M-1)

print(move)