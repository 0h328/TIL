import sys, math
sys.stdin = open('input.txt')

A, B = map(int, input().split())    # a진법의 수를 b진법으로
m = int(input())    # n자리수인 a진법 수
nums = list(map(int, input().split()))
dec = 0	# 10진법으로 만든 수
ans_list = []
res = ''

for i in range(m):
    dec += int(nums[i] * math.pow(A, m - i - 1))

while dec:
    tmp = dec % B
    ans_list.append(str(tmp))
    dec = dec // B

ans_list = ans_list[::-1]
res = ' '.join(ans_list)
print(res)