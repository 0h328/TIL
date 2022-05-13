import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
findNumber = {} # 번호로 포켓몬을 찾기 위한 dict
findWord = {}   # 포켓몬으로 번호를 찾기 위한 dict
for i in range(1, N+1): # 인덱스 1부터 시작
    p = sys.stdin.readline().rstrip()
    findNumber[i] = p   # key: 번호, value: 포켓몬
    findWord[p] = i     # key: 포켓몬, value: 번호

for i in range(M):
    find = sys.stdin.readline().rstrip()    # 찾으려고하는 포켓몬
    if find.isdigit():                      # input 타입이 숫자면
        print(findNumber.get(int(find)))    # findNumber에서 get
    else:                                   # input 타입이 문자면
        print(findWord.get(find))           # findWord에서 get

