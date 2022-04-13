import sys
sys.stdin = open('input.txt')

for _ in range(3):
    x = list(map(int, input().split()))
    if x.count(0) == 1:
        print('A')
    elif x.count(0) == 2:
        print('B')
    elif x.count(0) == 3:
        print('C')
    elif x.count(0) == 4:
        print('D')
    else:
        print('E')

