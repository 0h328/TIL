import sys
sys.stdin = open('input.txt')

x, y = map(int, input().split())

d = 0
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for i in range(x-1):
    d += month[i]
d = (d + y) % 7

print(week[d])