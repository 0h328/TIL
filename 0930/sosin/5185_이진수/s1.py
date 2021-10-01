import sys
sys.stdin = open('input.txt')

def xtob(s):
    tens = int('0x'+s, 16)
    return format(tens, 'b').zfill(4)

for T in range(int(input())):
    result = ''
    N, hex_word = input().split()

    for h in hex_word:
        result+=xtob(h)

    print('#{} {}'.format((T+1), result))