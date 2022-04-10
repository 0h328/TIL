import sys
sys.stdin = open('input.txt')

N = int(input())
file_1 = list(input())              # 첫번째 input을 기준으로 비교
for _ in range(N-1):                # N-1은 첫번째 input을 제외했기때문
    file_2 = list(input())          # 첫번째 input과 비교할 input
    for i in range(len(file_1)):
        if file_1[i] != file_2[i]:  # 각 자리수의 문자열이 같지 않으면
            file_1[i] = '?'         # 첫번째 input의 해당 자리수를 ?로 변경

print(''.join(file_1))  # 리스트 형식을 붙여서 문자열로 출력

