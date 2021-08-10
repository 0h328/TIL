import sys
sys.stdin = open('input.txt')

T = int(input())                         # 자료의 개수 입력
Numbers = list(map(int,input().split())) # 나열된 자료들을 리스트안에 패킹

max_value = Numbers[0]
for Number in Numbers:
    if max_value < Number:
        max_value = Number

counts = [0] * (max_value + 1)                 # 카운트 배열 # 0 ~ 16
temp = []                                      # 정렬된 배열

for i in range(0, T):
    counts[Numbers[i]] += 1

for i in range()