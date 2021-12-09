import sys
sys.stdin = open('input.txt')
'''
3 10 50 60 100 100 200 300
45 50 600 600 400 450 500 543
11 120 120 230 50 40 60 440
35 56 67 90 67 80 500 600
'''

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if (p1 < x2) or (q2 < y1) or (p2 < x1) or (q1 < y2):
        print('d')
    elif (x1 == p2 and y1 == q2) or (x2 == p1 and y1 == q2) or (x1 == p2 and q1 == y2) or (p1 == x2 and q1 == y2):
        print('c')
    elif y1 == q2 or q1 == y2:
        # if (x1 < x2 < p1) or (x1 < p2 < p1) or (x2 < x1 and p1 < p2) or (x1 == x2 and p1 == p2) or (x1 < x2 < p1 and x1 < p2 < p1):
        print('b')
    elif x1 == p2 or p1 == x2:
        # if (y1 < q2 < q1) or (y1 < y2 < q1) or (y2 < y1 and q1 < q2) or (y1 == y2 and q1 == q2) or (y1 < q2 < q1 and y1 < y2 < q1):
        print('b')
    else:
        print('a')

    # 조건문은 위에서 순서대로 걸러지면서 내려온다.


