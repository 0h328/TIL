"""
몇개의 조가 만들어지는지 원함 - 한명이 반드시 하나의 조에만 해당하므로 서로소집합(disjoint)
"""

import sys
sys.stdin = open('input.txt')



# def make_set(x):        # 학생들이 초기에 각자 본인이 조의 대표로 설정
#     student[x] = x


def union(x, y):                            # 학생 두명을 같은 조로 묶음 (x 의 대표자가 y의 대표자가 됨)
    student[find_set(y)] = find_set(x)      # 밑으로 들어가려는 학생의 대표 = 대표가 되려는 학생조의 대표를 찾음 


def find_set(x):                            # 해당 학생의 조 대표 찾기 및 대표자 한명으로 선정 / 해당 번호의 학생을 find_set 하게 되면 그 학생이 그 집합의 대표를 표시함
    if x != student[x]:
        student[x] = find_set(student[x])
    return student[x]

T = int(input())
answer = []

for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    student = [i for i in range(N+1)]       # 학생들 조의 대표가 누구인지 표시

    for idx in range(len(li)//2):           # 학생을 같은 조로 합침
        a = li[idx*2]
        b = li[idx*2 + 1]
        union(a, b)

    for i in range(1, N+1):                 # 마지막에 한번 모든 학생을 find_set 을 통해서 각자 조의 대표를 선택하도록 함
        find_set(i)

    answer.append('#{} {}'.format(tc, len(set(student))-1))

print(*answer, sep='\n')