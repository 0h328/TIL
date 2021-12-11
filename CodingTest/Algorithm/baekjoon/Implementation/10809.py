import sys
sys.stdin = open('input.txt')

S = input()

alp = list(range(97, 123))

for check in alp:
    print(S.find(chr(check)), end=' ')


# alp = ['a', 'b', 'c', 'd', 'e', 'f',
#        'g', 'h', 'i', 'j', 'k', 'l',
#        'm', 'n', 'o', 'p', 'q', 'r',
#        's', 't', 'u', 'v', 'w', 'x',
#        'y', 'z'
#        ]
#
# for check in alp:
#     if check in S:
#         print(S.index(check), end=' ')
#     else:
#         print(-1, end=' ')


# if 'a' in S:
#     print(S.index('a'), end=' ')
# else:
#     print(-1, end=' ')
# if 'b' in S:
#     print(S.index('b'), end=' ')
# else:
#     print(-1, end=' ')
# if 'c' in S:
#     print(S.index('c'), end=' ')
# else:
#     print(-1, end=' ')
# if 'd' in S:
#     print(S.index('d'), end=' ')
# else:
#     print(-1, end=' ')
# if 'e' in S:
#     print(S.index('e'), end=' ')
# else:
#     print(-1, end=' ')
# if 'f' in S:
#     print(S.index('f'), end=' ')
# else:
#     print(-1, end=' ')
# if 'g' in S:
#     print(S.index('g'), end=' ')
# else:
#     print(-1, end=' ')
# if 'h' in S:
#     print(S.index('h'), end=' ')
# else:
#     print(-1, end=' ')
# if 'i' in S:
#     print(S.index('i'), end=' ')
# else:
#     print(-1, end=' ')
# if 'j' in S:
#     print(S.index('j'), end=' ')
# else:
#     print(-1, end=' ')
# if 'k' in S:
#     print(S.index('k'), end=' ')
# else:
#     print(-1, end=' ')
# if 'l' in S:
#     print(S.index('l'), end=' ')
# else:
#     print(-1, end=' ')
# if 'm' in S:
#     print(S.index('m'), end=' ')
# else:
#     print(-1, end=' ')
# if 'n' in S:
#     print(S.index('n'), end=' ')
# else:
#     print(-1, end=' ')
# if 'o' in S:
#     print(S.index('o'), end=' ')
# else:
#     print(-1, end=' ')
# if 'p' in S:
#     print(S.index('p'), end=' ')
# else:
#     print(-1, end=' ')
# if 'q' in S:
#     print(S.index('q'), end=' ')
# else:
#     print(-1, end=' ')
# if 'r' in S:
#     print(S.index('r'), end=' ')
# else:
#     print(-1, end=' ')
# if 's' in S:
#     print(S.index('s'), end=' ')
# else:
#     print(-1, end=' ')
# if 't' in S:
#     print(S.index('t'), end=' ')
# else:
#     print(-1, end=' ')
# if 'u' in S:
#     print(S.index('u'), end=' ')
# else:
#     print(-1, end=' ')
# if 'v' in S:
#     print(S.index('v'), end=' ')
# else:
#     print(-1, end=' ')
# if 'w' in S:
#     print(S.index('w'), end=' ')
# else:
#     print(-1, end=' ')
# if 'x' in S:
#     print(S.index('x'), end=' ')
# else:
#     print(-1, end=' ')
# if 'y' in S:
#     print(S.index('y'), end=' ')
# else:
#     print(-1, end=' ')
# if 'z' in S:
#     print(S.index('z'), end=' ')
# else:
#     print(-1, end=' ')
