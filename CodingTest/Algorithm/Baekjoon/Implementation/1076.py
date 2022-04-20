import sys
sys.stdin = open('input.txt')

# case 1
# info = {'black': [0, 1],
#         'brown': [1, 10],
#         'red': [2, 100],
#         'orange': [3, 1000],
#         'yellow': [4, 10000],
#         'green': [5, 100000],
#         'blue': [6, 1000000],
#         'violet': [7, 10000000],
#         'grey': [8, 100000000],
#         'white': [9, 1000000000]
#         }
# multi = [1, 10, 100, 1000, 10000, 100000,
#          1000000, 10000000, 100000000, 1000000000]
#
# c1 = input()
# c2 = input()
# c3 = input()
#
# print(int(str(info[c1][0])+str(info[c2][0]))*info[c3][1])

# case 2
color = ['black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white',
        ]
c1 = color.index(input())
c2 = color.index(input())
c3 = color.index(input())

print(int(str(c1) + str(c2)) * (10 ** c3))
