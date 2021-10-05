# 미완료
# 현재 소요시간 1시간 34분

# thought process: 16분 21초
# 굳이 순열을 구현해야 할까?
# 그냥 정렬해서 확인하는게 나을지도
# visited도 필요x, 그래프 탐색이 아니고, 돌아올 위치도 없다.
# 조합을 구현해서 찾는게 빠를 듯 하다.

# implement process:
# 차례대로 돌아가며 한장씩 뽑고
# 각 선수 전용 리스트에 모든 숫자를 넣어서,
# 3 크기의 조합이 임시 저장될 배열 생성,
# 하나하나 조합을 정렬 시켜서, 만약 triplet or run 이면 그자리에서 스탑
# 먼저 찾는게 승자, 동시에 찾거나 끝까지 못 찾으면 무승부


import sys
sys.stdin = open('input.txt')

def comb (n, r):
    if r == 0:
        tmp1 = sorted(fl)
        tmp2 = sorted(sl)
        run, triplet = 0, 0
        for i in range(2):
            if tmp1[i] == tmp1[i+1]:
                run += 1
                if run == 2:
                    print(1)
                    return
            if tmp1[i] == tmp1[i+1] - 1:
                triplet += 1
                if triplet == 2:
                    print(1)
                    return
        run, triplet = 0, 0
        for i in range(2):
            if tmp2[i] == tmp2[i+1]:
                run += 1
                if run == 2:
                    print(2)
                    return
            if tmp2[i] == tmp2[i+1] - 1:
                triplet += 1
                if triplet == 2:
                    print(2)
                    return
        print(0)
        return
    elif n < r:
        print(0)
        return
    else:
        fl[r-1] = fp[n-1]
        sl[r-1] = sp[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


for tc in range(1, int(input())+1):

    cards = tuple(map(int, input().split()))
    fp = []
    fl = [0] * 3
    sp = []
    sl = [0] * 3

    for i in range(6):
        fp.append(cards[i * 2])
        sp.append(cards[i * 2 + 1])

    comb(6, 3)  # 각자 가지는 카드 개수, 카드 조합이 임시 저장 될 배열 길이