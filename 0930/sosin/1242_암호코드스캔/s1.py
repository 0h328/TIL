import sys
sys.stdin = open('input.txt')

def xtob(s):
    tens = int(s, 16)
    return format(tens, 'b').zfill(4) 

print(xtob('1'))
print(xtob('D'))
'1DB176C588D26EC'
# binary 7자리를 숫자로 변환 - 변환식에 따라
def bton(b):
    if b == '0001101':
        return 0
    elif b == '0011001':
        return 1
    elif b == '0010011':
        return 2
    elif b == '0111101':
        return 3
    elif b == '0100011':
        return 4
    elif b == '0110001':
        return 5
    elif b == '0101111':
        return 6
    elif b == '0111011':
        return 7
    elif b == '0110111':
        return 8
    elif b == '0001011':
        return 9

def change(word):
    if len(word) == 56:
        for i in range(8):
            print(word[7*i:7*(i+1)])
            print(bton(word[7*i:7*i+7]))
    else:
        word = word[2:-2]
        temp = 0
        result = 0
        for i in range(8):
            r = bton(word[7*i:7*i+7])
            if i%2 == 0:
                temp += 3*r
            else:
                temp += r
            result+=r
    if temp%10:
        return 0
    else:
        return result

for T in range(int(input())):
    result = 0
    row, col = map(int, input().split())
    for i in range(row):
        s = input().rstrip()
        j = 0
        while j < col:
            if s[j] != '0':
                temp = ''
                while s[j] != '0':
                    temp+=xtob(s[j])
                    j+=1
                print(temp)
                print(change(temp))
            j+=1
    break

    print('#{} {}'.format((T+1), result))


#1 38
#2 0
#3 36
#4 36
#5 44
#6 80
#7 76
#8 72
#9 182
#10 166
#11 212
#12 192
#13 1164
#14 1196
#15 1272
#16 1584
#17 4378
#18 6908
#19 7736
#20 6604
