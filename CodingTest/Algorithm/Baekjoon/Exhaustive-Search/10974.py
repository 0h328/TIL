import sys
sys.stdin = open('input.txt')

def backtracking():
    if len(ans) == N:
        print(*ans)
        return

    for i in range(1, N+1): # 1부터 N까지
        if i not in ans:    # i가 ans에 없으면
            ans.append(i)   # ans에 i를 추가
            backtracking()
            ans.pop()       # 다찼으면 숫자 하나씩 pop

N = int(input())
ans = []

backtracking()
