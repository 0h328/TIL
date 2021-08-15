import sys
sys.stdin = open('input.txt', encoding='UTF8')

def BruteForce(pattern, sentence):
    p, s = 0, 0
    cnt = 0
    while s < len(sentence):
        if p == len(pattern): # 패턴 검사 다 했으면 cnt + 1 하고 p 원상복구
            cnt += 1
            p = 0
        if sentence[s] != pattern[p]: # 문자와 패턴 다르면 s는 틀린 부분부터, p는 원상복구
            s = s - p + 1
            p = 0
        else: # 문자와 패턴 같으면 s, p 하나씩 더함
            s += 1
            p += 1
    if p == len(pattern): # while문 빠져나왔는데 마지막 문자가 패턴 맞으면 cnt + 1
        cnt += 1
    return cnt

#print(BruteForce('st', 'esfst')) # 패턴이 마지막에 걸려있는 경우 디버그테스트용


for _ in range(10):
    t = int(input())
    pattern = str(input())
    sentence = str(input())
    print('#{} {}'.format(t, BruteForce(pattern, sentence)))