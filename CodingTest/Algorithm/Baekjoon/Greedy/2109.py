import sys, heapq
sys.stdin = open('input.txt')

n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[1]))
p_list = []
for a in arr:
  heapq.heappush(p_list, a[0])
  if (len(p_list) > a[1]):
    heapq.heappop(p_list)

print(sum(p_list))