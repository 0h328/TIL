import sys
sys.stdin = open('input.txt')

N = int(input())
card = [i for i in range(1, N+1)]   # 1~7 숫자
answer = []                         # 버린 카드 집어넣기

while len(card) != 1:           # 길이가 1이 아닐동안만. 왜? 빈 리스트는 pop하면 에러발생
    answer.append(card.pop(0))  # 첫번째 수 버리고, answer에 추가
    card.append(card.pop(0))    # 그 다음 수는 뒤로 보내고

for ans in answer:
    print(ans, end=' ')
print(card[0])  # 최종적으로 남아 있는 수까지 출력