import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

info = {}

for _ in range(N):
    address, password = input().rstrip().split()
    info[address] = password

for i in range(M):
    address = input()
    print(info[address])

