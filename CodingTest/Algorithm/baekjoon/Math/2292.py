import sys
sys.stdin = open('input.txt')

N = int(input())

hive = 1
cnt = 1
while N > hive:
    hive += 6 * cnt
    cnt += 1

print(cnt)
