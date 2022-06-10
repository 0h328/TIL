import sys
sys.stdin = open('input.txt')

find_str = input()
N = int(input())

cnt = 0
for _ in range(N):
    ring = input()
    ring = ring + ring  # 시작과 끝이 연결되어있으므로 하나를 더해준다.

    if ring.find(find_str) != -1:   # find하지 못하면 -1이므로, -1이 아닌경우는 문자열이 있는 경우
        cnt += 1

print(cnt)