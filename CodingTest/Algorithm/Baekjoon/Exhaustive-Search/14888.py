import sys
sys.stdin = open('input.txt')

def solution(num, idx, add, sub, mul, div):
    global max_num, min_num
    if idx == N:    # 주어진 수를 모두 연산한 경우
        max_num = max(max_num, num) # 최댓값 갱신
        min_num = min(min_num, num) # 최솟값 갱신
        return

    if add:
        solution(num+nums[idx], idx+1, add-1, sub, mul, div)    # 연산할때마다 idx+1, 해당 연산 개수-1
    if sub:
        solution(num-nums[idx], idx+1, add, sub-1, mul, div)
    if mul:
        solution(num*nums[idx], idx+1, add, sub, mul-1, div)
    if div:
        solution(int(num/nums[idx]), idx+1, add, sub, mul, div-1)

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
a, s, m, d = map(int, input().split())  # 덧셈, 뺄셈, 곱셈, 나눗셈

max_num = -10e9 # -10억보다 크거나 같음
min_num = 10e9  # 10억보다 작거나 같음

solution(nums[0], 1, a, s, m, d)        # 첫번째 인자부터 시작, idx 0은 사용했으므로 1부터 시작, 사칙연산은 매개변수로
print(max_num)
print(min_num)
