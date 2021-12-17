import sys
sys.stdin = open('input.txt')

word = input()
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 풀이1
N = len(word)
if 'dz' not in word:    # dz가 문자열에 포함되지 않은 경우
    for c in croa:      # croa를 돌면서
        if word.count(c) > 1:   # 요소 여러개가 중복되어 문자열에 있는 경우
            N -= len(c)*word.count(c)   # 개수 x 길이를 빼주고
            N += word.count(c)  # 개수만큼 다시 더해줌
        elif c in word: # 요소가 중복되지 않고, 문자열에 포함되어있는 경우
            N -= len(word[word.index(c):word.index(c) + len(c)])    # 문자열 내 해당 요소 위치 인덱스 부분의 길이를 빼고
            N += 1  # 뺀 인덱스 범위만큼 +1

else:   # dz가 문장졀에 포함된 경우
    N -= word.count('dz=')*3    # 문자열 내 'dz=' 개수 x 'dz=' 길이를 빼고
    N += word.count('dz=')      # 'dz=' 문자열 개수 만큼 다시 더함
    word = word.replace('dz=', 'X') # 'dz='를 임의 문자로 바꾸고
    for c in croa:  # croa를 돌면서
        if word.count(c) > 1:   # 요소 여러개가 중복되어 문자열에 있는 경우
            N -= len(c)*word.count(c)   # 개수 x 길이를 빼주고
            N += word.count(c)  # 개수만큼 다시 더해줌
        elif c in word: # 요소가 중복되지 않고, 문자열에 포함되어있는 경우
            N -= len(word[word.index(c):word.index(c) + len(c)])    # 문자열 내 해당 요소 위치 인덱스 부분의 길이를 빼고
            N += 1  # 뺀 인덱스 범위만큼 +1

print(N)

# 풀이2
# for c in croa:
#     word = word.replace(c, 'X')
#
# print(len(word))
