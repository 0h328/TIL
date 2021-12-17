import sys
sys.stdin = open('input.txt')

N = list(input())
N.sort(reverse=True)
res = ''.join(N)
print(int(res))
