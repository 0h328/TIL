import sys
from itertools import permutations
sys.stdin = open('input.txt')

k = int(input())
signs = input().split()

res = []
for p in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k+1):
  flag = True
  for i in range(len(signs)):
    if signs[i] == '<':
      if p[i] < p[i+1]:
        continue
      else:
        flag = False
        break
    else:
      if p[i] > p[i+1]:
        continue
      else:
        flag = False
        break
  if flag:
    res.append(p)

print(''.join(map(str, list(max(res)))))
print(''.join(map(str, list(min(res)))))