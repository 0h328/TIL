import sys
sys.stdin = open('input.txt')

K = int(input())

a = [1, 0]
b = [0, 1]

for i in range(2, K+1):
    a_num = a[i-1] + a[i-2]
    a.append(a_num)
    b_num = b[i-1] + b[i-2]
    b.append(b_num)

print(a[K], b[K])