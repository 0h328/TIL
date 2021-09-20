import sys
sys.stdin = open('input.txt')

# thought process: 2분 59초
# 하나씩 대조, 일치하면 target idx 증가 후 대조 반복
# 틀리면 타겟 인덱스 초기화 & 전체 인덱스 한칸 전진 후 다시 대조 시작
# target idx 끝까지 가면, 일치하니, 바로 루프 return 1
# 루프를 나와버리면 없다는뜻이니 return 0

# 소요시간 12분 4초
def checker():
    for i in range(f-t+1):
        for j in range(t):
            if target[j] != full[i + j]:
                break
            elif j == t - 1:
                return 1
    return 0

for tc in range(1, int(input())+1):
    target = input()
    full = input()
    t = len(target)
    f = len(full)
    print('#{} {}'.format(tc, checker()))

# 소요시간: 4분35초
# for tc in range(1, int(input())+1):
#     target = input()
#     main_str = input()
#
#     if target in main_str:
#         print(1)
#     else:
#         print(0)
