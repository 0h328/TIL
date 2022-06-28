import sys
sys.stdin = open('input.txt')

# 1
read = lambda: sys.stdin.readline().rstrip()

N, L = map(int, read().split())
h = list(map(int, read().split()))
h.sort()

for fruit in h:
    if fruit > L:
        break
    elif fruit <= L:
        L += 1

print(L)

# 2
# n, l = map(int, input().split())
# fruit = list(map(int, input().split()))
# fruit.sort()
#
# for i in range(len(fruit)):
#   if l >= fruit[i] :
#     l += 1
#
# print(l)