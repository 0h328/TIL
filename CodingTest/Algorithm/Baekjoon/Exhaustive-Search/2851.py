import sys
sys.stdin = open('input.txt')

mush = []
score = 0
for i in range(10):
    mush.append(int(input()))

for m in mush:
    score += m
    if score >= 100:
        if score - 100 > 100 - (score - m):
            score -= m
        break
print(score)