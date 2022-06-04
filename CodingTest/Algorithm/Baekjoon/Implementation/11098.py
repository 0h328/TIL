import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
for _ in range(n):
    p = int(sys.stdin.readline())
    info = {}
    for _ in range(p):
        c, name = sys.stdin.readline().split()
        info[int(c)] = name

    print(info[max(info.keys())])


