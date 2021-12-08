import sys
sys.stdin = open('input.txt')

H, M = map(int, input().split())

if 1 <= H <= 23:
    if 45 <= M <= 59:
        M -= 45
    elif M <= 44:
        M += 15
        H -= 1
elif H == 0:
    if 45 <= M <= 59:
        M -= 45
    elif M <= 44:
        M += 15
        H += 23

print(H, M)