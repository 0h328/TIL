import sys
sys.stdin = open('input.txt')

x = int(input())
y = int(input())

def quadrant():
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

print(quadrant())
