import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    iron_stick = input()
    l = len(iron_stick)
    lazer = 0
    stick = 0
    cnt = 0

    for i in range(l):
        if iron_stick[i] == '(':
            if iron_stick[i+1] == ')':
                lazer = 1
            else:
                stick += 1
        else:
            if lazer == 1:
                cnt += stick
                lazer = 0
            else:
                cnt += 1
                stick -= 1
    print(cnt)












"""
#1 17
#2 24
"""