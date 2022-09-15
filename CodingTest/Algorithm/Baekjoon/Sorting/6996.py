import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for i in range(T):
    a, b = map(str, sys.stdin.readline().split())

    x = sorted(list(a))
    y = sorted(list(b))

    if x == y:
        print("%s & %s are anagrams." % (a, b))
    else:
        print("%s & %s are NOT anagrams." % (a, b))