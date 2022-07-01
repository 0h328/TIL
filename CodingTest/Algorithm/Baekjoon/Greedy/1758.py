import sys
sys.stdin = open('input.txt')

N = int(input())
arr = []
for _ in range(N):
  arr.append(int(input()))

arr.sort(reverse=True)

res = 0
for i in range(N):
  val = arr[i] - ((i+1)-1)
  if val > 0:
    res += val

print(res)