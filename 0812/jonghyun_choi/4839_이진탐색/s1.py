import sys
sys.stdin = open('input.txt')

T = int(input())

def find_page(total_page,search_page):    # Page 검색 수를 count해주는 함수 생성
    l = 1                                 # 시작 페이지
    r = total_page                        # 마지막 페이지 : total_page
    cnt = 0                               # 검색 수 count 해주는 cnt 변수 초기화
    while l <= r:                         # 검색 시작 페이지가 검색 끝 페이지 보다 크지 않을 때까지
        c = (l + r) //2                   # 중간 페이지 식 c = int((l+r)/2)
        cnt += 1                          # 중간 페이지가 만들어지는 것 = 검색 수 1 증가
        if c == search_page:              # 중간 페이지가 찾는 페이지와 같으면 cnt를 반환하며 함수 종료
            return cnt
        elif c < search_page:             # 중간 페이지가 찾는 페이지보다 작으면 검색 시작 페이지를 해당 중간 페이지로 업데이트
            l = c
        else:                             # 중간 페이지가 찾는 페이지보다 크면 검색 끝 페이지를 해당 중간 페이지로 업데이트
            r = c
    if l > r:                             # 검색할 search page가 total page보다 큰 edge case 대비하는 코드
        return total_page + 1             # 검색 수가 작을 수록 이기는 것이기 때문에 못 찾을 경우 total page보다 1 큰 값으로 반환


for Case in range(T):
    P, A, B = map(int,input().split())

    a_count = find_page(P,A)              # 위에서 작성한 find_page 함수를 이용하여 A가 검색할 때 필요한 count 얻기
    b_count = find_page(P,B)              # 위에서 작성한 find_page 함수를 이용하여 B가 검색할 때 필요한 count 얻기

    if a_count == b_count:                # A와 B의 count가 같으면 0 출력
        print('#{} {}'.format(Case+1,0))
    elif a_count > b_count:               # A가 B보다 크면 B 출력
        print('#{} {}'.format(Case+1,'B'))
    else:                                 # A가 B보다 작으면 A 출력
        print('#{} {}'.format(Case+1,'A'))



