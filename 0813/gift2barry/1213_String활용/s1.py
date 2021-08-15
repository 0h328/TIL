import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# thought process:
# 무어 알고리즘 구현해보려 노력
# 패턴의 끝부분 비교
# 틀리면 패턴의 뒤에 문자를 순차적으로 비교
# 있으면 일치된 인풋문자열인덱스 - 패턴문자열인덱스 만큼 앞으로 패턴문자열 이동하고 패턴의 끝부분 비교
# 만약 일치되는 문자 없으면, 패턴 문자열 길이만큼 이동

# for tc in range(1, 2):
#
#     tc_idx = int(input())
#     p = input()
#     arr = input()
#
#     if p[-1] == arr[len(p)-1]:

for tc in range(1, 11):

    tc_idx = int(input())
    p = list(input())
    arr = list(input())

    for i in range(len(p))