"""
연습 문제 5.
16진수 문자로 이루어진 1차원 배열이 주어질 때 암호비트패턴을 찾아 차례대로 출력하시오. (암호는 연속되어있다.)

암호비트패턴
0  001101
1  010011
2  111011
3  110001
4  100011
5  110111
6  001011
7  111101
8  011001
9  101111

입력 예시)
0DEC

0269FAC9A0

출력 예시)
0 2

1 1 7 8 0


참고)
0DEC
-> 0 0 0 0 1 1 0 1 1 1 1 0 1 1 0 0
-> 0 0 / 0 0 1 1 0 1 / 1 1 1 0 1 1 / 0 0
              0            2
"""
# 16진수 -> 2진수
asc = [[0, 0, 0, 0],  #0
       [0, 0, 0, 1],  #1
       [0, 0, 1, 0],  #2
       [0, 0, 1, 1],  #3
       [0, 1, 0, 0],  #4
       [0, 1, 0, 1],  #5
       [0, 1, 1, 0],  #6
       [0, 1, 1, 1],  #7
       [1, 0, 0, 0],  #8
       [1, 0, 0, 1],  #9
       [1, 0, 1, 0],  #A
       [1, 0, 1, 1],  #B
       [1, 1, 0, 0],  #C
       [1, 1, 0, 1],  #D
       [1, 1, 1, 0],  #E
       [1, 1, 1, 1]]  #F

# 암호비트패턴
code = [[[[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)]
code[0][0][1][1][0][1] = 0
code[0][1][0][0][1][1] = 1
code[1][1][1][0][1][1] = 2
code[1][1][0][0][0][1] = 3
code[1][0][0][0][1][1] = 4
code[1][1][0][1][1][1] = 5
code[0][0][1][0][1][1] = 6
code[1][1][1][1][0][1] = 7
code[0][1][1][0][0][1] = 8
code[1][0][1][1][1][1] = 9

# ASCII -> Hexadecimal
def ascii_to_hex(c):
    # 9 이하
    if c <= '9':
        return ord(c) - ord('0')
    # 10 이상
    else:
        return ord(c) - ord('A') + 10

def hex_to_binary(x):
    global pos
    for i in range(4):
        t.append(asc[x][i])

t = []
# 암호
arr = '0DEC'
# arr = '0269FAC9A0'

ans = []
pos = -1

for i in range(len(arr)):
    hex_to_binary(ascii_to_hex(arr[i]))

# 뒤에서 1 찾기
for i in range(len(t)-1, -1, -1):
    if t[i] == 1:
        pos = i
        break

while pos - 6 > 0:
    x = code[t[pos-5]][t[pos-4]][t[pos-3]][t[pos-2]][t[pos-1]][t[pos]]
    ans.append(x)
    pos -= 6

# print(ans)
for i in range(len(ans)):
    print(ans.pop(), end=' ')
print()