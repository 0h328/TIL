'''
만약에 “AGCAT"와 ”GGAAT"는 첫 번째 글자와 세 번째 글자가 다르므로
Hamming Distance는 2이다.

A G C A T
G G A A T
1 0 1 0 0 => 1+0+1+0+0 = 2

1번째 DNA = T A T G A T A C
2번째 DNA = T A A G C T A C
3번째 DNA = A A A G A T C C
4번째 DNA = T G A G A T A C
5번째 DNA = T A A G A T G T
최대빈도문자 T A A G A T A C (위 5개 DNA 중 가장 많이 나온 문자)
문자의 개수  1 1 1 0 1 0 2 1 (가장 많이 나온 문자를 제외한 문자 개수)
Hamming Distance = 1+1+1+0+1+0+2+1 = 7
'''

import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

dna = []
for _ in range(N):
    dna.append(input())

cnt = 0
dna_res = ''
for i in range(M):
    a, c, g, t = 0, 0, 0, 0     # DNA의 각 idx 별로 나온 문자 개수 확인
    for j in range(N):
        if dna[j][i] == 'A':    # DNA의 첫번째 문자가 'A'
            a += 1
        elif dna[j][i] == 'C':  # DNA의 첫번째 문자가 'C'
            c += 1
        elif dna[j][i] == 'G':  # DNA의 첫번째 문자가 'G'
            g += 1
        else:                   # DNA의 첫번째 문자가 'T'
            t += 1
    cnt += N - max(a, c, g, t)  # 합이 가장 작은 DNA를 구해야하므로 전체 DNA 개수에서 가장 많이 나온 문자의 개수를 뺀다.
    # 가장 많이 나온 문자끼리 합성한 문자 구하기
    if max(a, c, g, t) == a:
        dna_res += 'A'
    elif max(a, c, g, t) == c:
        dna_res += 'C'
    elif max(a, c, g, t) == g:
        dna_res += 'G'
    else:
        dna_res += 'T'

print(dna_res)
print(cnt)

# 딕셔너리 풀이
# N, M = map(int, input().split())
#
# DNA_lst = []
#
# for i in range(N):
#     DNA = input()
#     DNA_lst.append(DNA)
#
# differ = 0
# strng = ""
#
# for i in range(M):
#     dct = {}
#     for DNAS in DNA_lst:
#         if DNAS[i] in dct:
#             dct[DNAS[i]] += 1
#         else:
#             dct[DNAS[i]] = 1
#     dct = list(dct.items())
#     dct.sort(key=lambda x:(-x[1],x[0]))
#     strng += dct[0][0]
#     differ += N - dct[0][1]
#
# print(strng)
# print(differ)


