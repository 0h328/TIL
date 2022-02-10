import sys
sys.stdin = open('input.txt')

K = int(input())
for i in range(1, K+1):
    X = list(map(int, input().split()))
    sorted_X = sorted(X[1:], reverse=True)
    print('Class', i)

    gap = 0
    for j in range(X[0]-1):
        gap = max(sorted_X[j]-sorted_X[j+1], gap)

    print('Max', str(max(X[1:]))+',', 'Min', str(min(X[1:]))+',', 'Largest gap', gap)