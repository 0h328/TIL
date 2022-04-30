import sys
sys.stdin = open('input.txt')

X, Y = map(int, input().split())
# 1단계 : 역순으로 만들어야 하므로 문자화 시킨다.
X, Y = str(X), str(Y)

# 2단계 : 문자화시킨 input값을 역순으로 바꾸고, 문자 내 0을 모두 지운다.
X, Y = X[::-1].strip('0'), Y[::-1].strip('0')

# 3단계 : 문자를 정수화 시켜서 Rev(X) + Rev(Y)를 한다.
ans = int(X) + int(Y)

# 4단계 : 다시 문자화 시키고 역순으로 바꾸고, 문자 내 0을 모두 지운다.
ans = str(ans)[::-1].strip('0')

print(ans)