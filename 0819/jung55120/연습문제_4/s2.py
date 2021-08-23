# global 영역부터 각 함수의 고유한 영역을 디버거에서 확인해보세요!

n = 10

def f1(a):
    f2(a)

def f2(b):
    f3(b)

def f3(c):
    print(c**2)

f1(n) # 100