import sys
sys.stdin = open('input.txt')

n, m = map(int, sys.stdin.readline().split())

cards = []
cards += map(int, sys.stdin.readline().split())

for _ in range(m):
    cards.sort()
    cards[0] = cards[1] = cards[0] + cards[1]

print(sum(cards))