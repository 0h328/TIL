import sys
sys.stdin = open('input.txt')

cha = input()
dia = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

ans = 0
for i in range(len(cha)):
    for d in dia:
        if cha[i] in d:
            ans += dia.index(d) + 3

print(ans)
