import sys
sys.stdin = open('input.txt')

codes_key = {0:'0001101', 1:'0011001', 2:'0010011', 3:'0111101', 4:'0100011', 
                5:'0110001', 6:'0101111', 7:'0111011', 8:'0110111', 9:'0001011'}

def change():
    global result
    for m in range(8):
        for h in range(10):
            if codes_key[h] == codes[m] :
                result[m] = h

    temp = 0
    code = 0
    for i in range(8):
        if i%2==0:
            temp += result[i]*3
        else :
            temp += result[i]
        code += result[i]
 
    if (temp)%10:
        return 0
    return code
 
for T in range(int(input())):
    N, M = map(int, input().split())
    s = list(input() for _ in range(N))
    codes = []
    result = [0] * 8
    for arr in s:
        i = M-1
        while i>0 :
            if arr[i] == '1' :
                codes.append(arr[i-6:i+1])
                i -= 6
            i -= 1
        if len(codes) > 0:
            codes = codes[::-1]
            break
 
    print('#{} {}'.format((T+1), change()))

#1 38 
#2 0 
#3 34
#4 28
#5 24
#6 26
#7 36
#8 30
#9 0
#10 34