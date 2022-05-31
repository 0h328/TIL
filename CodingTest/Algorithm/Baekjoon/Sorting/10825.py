import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
info = [list(sys.stdin.readline().split()) for _ in range(N)]

# 국어 : 감소
# 국어 점수가 같으면 영어 점수 : 증가
# 국영 점수 같으면 수학 점수 : 감소
# 다 같으면 이름 사전순
info.sort(key=lambda info: (-int(info[1]), int(info[2]), -int(info[3]), info[0]))

for i in info:
    print(i[0])