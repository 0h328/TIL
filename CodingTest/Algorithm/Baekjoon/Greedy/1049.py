import sys
sys.stdin = open('input.txt')

n, m = map(int, sys.stdin.readline().split())
min_p, min_pi = 1000, 1000

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    min_p = min(min_p, a)
    min_pi = min(min_pi, b)
cnt = n // 6 + 1

m_result = 100000000
for i in range(cnt + 1):
    result = 0
    tmp = n
    tmp -= i * 6
    result += i * min_p
    if tmp > 0:
        result += tmp * min_pi
    m_result = min(m_result, result)
print(m_result)