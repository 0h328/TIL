import sys
sys.stdin = open('input.txt')

# thought process: 4분35초
# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN" 리스트 생성
# 하나씩 돌아가며 count 함수로 인풋 리스트 안에 해당 문자열 개수를 확인
# 하댕 개수 만큼 새로운 리스트에 문자열 저장
# 위에 process를 반복

# 소요시간: 9분 7초
for tc in range(1, int(input())+1):

    T, num_len = map(str, input().split())
    random_nums = list(map(str, input().split()))

    num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    new_num_list = []
    for i in num_list:
        cnt = random_nums.count(i)
        for j in range(cnt):
            new_num_list.append(i)
    print(T)
    print(*new_num_list)