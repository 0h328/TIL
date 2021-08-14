import sys
sys.stdin = open('input.txt')

planets = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for _ in range(int(input())):
    T, _ = input().split()
    words = input().split()
    result = []
    for p in planets:
        result.extend([p]*words.count(p))

    print(T)
    print(*result)
