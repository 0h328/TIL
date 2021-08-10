import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    boxes = list(map(int, input().split()))
    max_drop = 0
    for idx1 in range(len(boxes) - 1):
        cnt = 0
        for idx2 in range(idx1 + 1, len(boxes)):
            if boxes[idx1] <= boxes[idx2]:
               cnt += 1
        drop = N - idx1 - 1 - cnt
        if max_drop < drop:
            max_drop = drop
    print(max_drop)