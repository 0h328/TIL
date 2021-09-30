import sys
sys.stdin = open('input.txt')


def ascii_to_hex(c):
    if c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10


def hex_to_bin(c):
    tmp = c
    stack = []
    global result
    while tmp > 0:
        stack.append(tmp % 2)
        tmp //= 2
    while len(stack) < 4:
        stack.append('0')
    while stack:
        result += str(stack.pop())

T = int(input())

for tc in range(1, T+1):
    N, h = input().split()
    result = ''
    for i in range(len(h)):
        hex_to_bin(ascii_to_hex(h[i]))

    print('#{} {}'.format(tc, result))
