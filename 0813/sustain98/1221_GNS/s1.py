import sys
sys.stdin = open('input.txt')

d = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
t = int(input())
for _ in range(t):
    idx, length = input().split()
    test_case = list(input().split())

    test_case.sort(key=lambda x: d[x])
    print(idx)
    print(' '.join(test_case))