import sys
sys.stdin = open('input.txt')

data_list = list(map(int,input().split()))

max_value = data_list[0]  # max_value를 구하는 이유는 리스트 초기화 시 리스트 크기를 정해주기 위함.

for data in data_list:
    if data > max_value:
        max_value = data

# print(max_value)

cnt = [0]*(max_value+1)  # max_value의 크기만큼 cnt 리스트가 생성.
                         # 1을 더해준 이유는 0값도 있을 수 있기 때문

for data in data_list:
    cnt[data] += 1       # data_list를 순회하면서 각각의 값의 갯수를 구함.
# print(cnt)

for i in range(1,len(cnt)):  # cnt 리스트를 값의 개수를 나타내는 리스트에서 누적값을 구하는 리스트로 변경
    cnt[i] += cnt[i-1]       # 누적을 해주는 이유 : 원활한 인덱싱을 위하여
# print(cnt)
sorted_list = [0]* cnt[-1]  # sorted_list의 크기는 값의 갯수 (data_list의 크기)
# print(sorted_list)
for ind in range(len(data_list)-1,-1,-1): # 데이터 리스트를 거꾸로 순회 시작. 거꾸로 순회하는 이유는 원래 있던 자리를 그대로 맞춰 주기 위함.
    sorted_list[cnt[data_list[ind]]-1] = data_list[ind] # 각각 채워나갈 때마다 하나씩 빼주기 시작함.
    cnt[data_list[ind]] -= 1
print(sorted_list)

