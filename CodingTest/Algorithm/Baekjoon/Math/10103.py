import sys
sys.stdin = open('input.txt')

n = int(input())

cy_s = 100
sd_s = 100
for _ in range(n):
    cy, sd = map(int, input().split())

    if cy < sd:
        cy_s -= sd
    elif cy > sd:
        sd_s -= cy

print(cy_s)
print(sd_s)