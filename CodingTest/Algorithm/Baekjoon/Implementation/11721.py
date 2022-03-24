import sys
sys.stdin = open('input.txt')

a = input()

for i in range(0, len(a), 10):
    print(a[i:i+10])