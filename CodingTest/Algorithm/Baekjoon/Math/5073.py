import sys
sys.stdin = open('input.txt')

while True:
    tri = sorted(list(map(int, input().split())))

    if tri[0] == tri[1] == tri[2] == 0:
        break
    if tri[0]+tri[1] <= tri[2]:
        print("Invatrid")
    elif tri[0] == tri[1] == tri[2]:
        print("Equilateral")
    elif tri[0] == tri[1] or tri[1] == tri[2] or tri[2] == tri[0]:
        print("Isosceles")
    else:
        print("Scalene")