import sys
sys.stdin = open('input.txt')

ans = 0
for _ in range(5):
    score = int(input())

    if score >= 40:
        ans += score
    else:
        ans += 40

print(ans//5)
