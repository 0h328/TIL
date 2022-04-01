import sys
sys.stdin = open('input.txt')

N = int(input())

# 1,2,3,4 -> 0의 개수 : 0개

cnt = 0
while N >= 5:
    cnt += N//5 # 1,2,...
    N //= 5

print(cnt)