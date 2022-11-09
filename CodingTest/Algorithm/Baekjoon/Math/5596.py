import sys
sys.stdin = open('input.txt')

MK = sum(list(map(int, input().split())))
MS = sum(list(map(int, input().split())))

print(MK if MK == MS else max(MK, MS))


