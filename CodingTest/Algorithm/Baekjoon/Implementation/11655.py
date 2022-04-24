import sys
sys.stdin = open('input.txt')

string = input()
ans = ''

# 65~90 : A~Z, 97~122 : a~z
for str in string:
    if 'A' <= str and str <= 'Z':
        str = ord(str) + 13
        if str > 90:    # Z를 넘어가면
            str -= 26   # 26을 빼서 A부터 다시 돌아가게함
        ans += chr(str)
    elif 'a' <= str and str <= 'z':
        str = ord(str) + 13
        if str > 122:   # z를 넘어가면
            str -= 26   # 26을 빼서 a부터 다시 돌아가게함
        ans += chr(str)
    else:
        ans += str

print(ans)