import sys
sys.stdin = open('input.txt')

while True:
    try:
        print(input())
    except EOFError:
        break