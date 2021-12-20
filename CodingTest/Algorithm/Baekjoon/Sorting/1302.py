import sys
sys.stdin = open('input.txt')

N = int(input())

book = []
for _ in range(N):
    book.append(input())

book_dict = {}      # 책의 종류: 권 수 형태의 딕셔너리로 구성
for b in book:
    book_dict[b] = book_dict.get(b, 0) + 1 # 책의 종류가 나올때마다 +1

num = max(book_dict.values())   # num 변수를 가장 많은 책의 수만큼 지정
sold_list = []
for k, v in book_dict.items():  # key, value를 돌면서
    if num == v:                # 가장 많은 책의 수와 value가 같으면
        sold_list.append(k)     # 가장 많은 책 종류를 리스트에 추가

sold_list.sort() # 사전 순으로 정렬
print(sold_list[0])


