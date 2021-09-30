import sys
sys.stdin = open('input.txt')


# thought process:
# 16진수를 2진수로 바꿔야한다.
# 고로, 16진수 => 10진수 => 2진수 변형?

# 돌아가면서 각 문자들 사이에0을 넣고
# 시프트 연산을 하며



# 질문1: why shift 연산자를 사용하는가
# 질문2: 마스킹을 하는 이유와 효과


# int(input())
# for tc in range(1, 2):
#
#     N, L = input().split()
#     ans = []
#     for i in range(int(N)):     # 16진수 글자 수 만큼 반복
#         tmp = int(L[i], 16)     # 10진수로 변환
#         ans.append(bin(tmp))    # 2진수로 변환
#         print(tmp)
#
#     print(*ans)

print((0x0304 >> 8) & 0xff)
# 질문3: why 우측으로 8 shift 하면 04 delete?


# 0x04는 16진수에서 숫자 4이고, 여기서 시프트 연산 시,
# 2진수 모양을 기준으로 우측으로 두번 시프트,
# 0100 에서 0001 이 되어 십진수 1 이 된다.
