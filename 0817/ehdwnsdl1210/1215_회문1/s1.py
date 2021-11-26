import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(8)]

    print(arr)