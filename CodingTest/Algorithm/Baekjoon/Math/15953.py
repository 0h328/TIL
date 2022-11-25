import sys
sys.stdin = open('input.txt')

def first_festival(prize):
    if a == 1:
        return 5000000
    elif 1 < a <= 3:
        return 3000000
    elif 3 < a <= 6:
        return 2000000
    elif 6 < a <= 10:
        return 500000
    elif 10 < a <= 15:
        return 300000
    elif 15 < a <= 21:
        return 100000
    else:
        return 0

def second_festival(prize):
    if b == 1:
        return 5120000
    elif 1 < b <= 3:
        return 2560000
    elif 3 < b <= 7:
        return 1280000
    elif 7 < b <= 15:
        return 640000
    elif 15 < b <= 31:
        return 320000
    else:
        return 0

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(first_festival(a) + second_festival(b))





