import sys
sys.stdin = open('input.txt')

total = int(input())
books = []
for _ in range(9):
    books.append(int(input()))

print(total - sum(books))