import sys
sys.stdin = open('input.txt', encoding='UTF8')

for _ in range(1, 11):
    t = input()
    p = input()
    m = input()
    result = m.count(p)
    print("#{0} {1}".format(t, result))