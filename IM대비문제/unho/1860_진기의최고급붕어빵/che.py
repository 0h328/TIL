import sys
sys.stdin = open('joon.txt')

one = [input() for _ in range(1000)]

sys.stdin = open('out.txt')

two = [input() for _ in range(1000)]

for i in range(1000):
    if one[i] != two[i]:
        print(i)