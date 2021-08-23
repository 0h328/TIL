n = 10

def f1(a):
    f2(a)

def f2(b):
    f3(b)

def f3(c):
    print(c**2)

f1(n) # 100