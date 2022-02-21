import sys
sys.stdin = open('input.txt')

score = [int(input()) for _ in range(8)]

sorted_score = sorted(score, reverse=True)[:5]  # 상위 5개 점수까지만 자르기
ans = []
for i in sorted_score:
    ans.append(score.index(i)+1)

ans.sort()
print(sum(sorted_score))
print(*ans)


