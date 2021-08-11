import sys
sys.stdin = open('input.txt')

T = int(input())                         # 자료의 개수 입력
numbers = list(map(int,input().split())) # 나열된 자료들을 리스트안에 패킹

max_value = numbers[0]
for number in numbers:
    if max_value < number:
        max_value = number

counts = [0] * (max_value + 1)                 # 카운트 배열 # 0 ~ 16
print(counts)
temp = [0] * T                                 # 정렬된 배열

for i in range(0, len(numbers)):
    counts[numbers[i]] += 1
print(counts)

for i in range(1, len(counts)):
    counts[i] += counts[i-1]
print(counts)

for i in range(len(numbers)-1, -1, -1):
    temp[counts[numbers[i]] - 1] = numbers[i]
    # counts는 누적된 상태임.
    counts[numbers[i]] -= 1

print(temp)