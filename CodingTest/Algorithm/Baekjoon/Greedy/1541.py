import sys
sys.stdin = open('input.txt')

f = input().split('-')      # -가 나오기전까지는 모두 +를 해야하므로 - 기준으로 나눔

# print(f[0].split('+'))
ans = 0
for i in f[0].split('+'):   # idx 0번째는 -나오기 전까지 수로 이루어졌으므로, 모두 더한다.
    ans += int(i)

for i in f[1:]:             # 이후 idx 1번째부터는 숫자 하나로만 되어있거나, +와 함께 연산식으로 되어있는 식 중에서
    for j in i.split('+'):  # 그 다음 +를 기준으로 split하고
        ans -= int(j)       # 그 숫자들을 빼준다.

print(ans)

