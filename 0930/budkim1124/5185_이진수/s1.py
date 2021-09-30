import sys
sys.stdin = open("input.txt")


sol_dict = {'0':0,'1':1, '2':2, '3':3, '4':4,'5':5,'6':6,'7':7,'8':8, '9':9,'A':10,'B':11,'C':12, 'D':13,'E':14,'F':15}

def bin(number):
    global tmp
    for _ in range(4):
        quotient = number // 2  # 몫
        remainder = number % 2  # 나머지
        tmp = str(remainder) + tmp
        number = quotient
    return

T = int(input())
for t in range(T):
    N, num = map(str, input().split())

    result = ''
    for i in num:
        tmp = ''
        bin(sol_dict[i])
        result += tmp
    print('#{} {}'.format(t+1, result))