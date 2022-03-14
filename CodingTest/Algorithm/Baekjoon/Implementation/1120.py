import sys
sys.stdin = open('input.txt')

A, B = input().split()

ans = []
for i in range(len(B)-len(A)+1):
    cnt = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            cnt += 1
    ans.append(cnt)

print(min(ans))

# koder = (topco)der
# koder = t(opcod)er
# koder = to(pcode)r
# koder = top(coder)
# 이런식으로 비교해서 최소 개수를 출력한다.