import sys
sys.stdin = open('input.txt')

S = list(input())
T = list(input())

while len(T) != len(S):     # T와 S의 길이가 같아질때까지 T를 하나씩 슬라이싱
    if T[-1] == 'B':        # 마지막 idx가 B면
        T = T[:-1][::-1]    # 마지막 idx 없애고(pop), 문자열 뒤집기
    else:                   # A면
        T = T[:-1]          # 마지막 idx 없애기

print(1 if S == T else 0)