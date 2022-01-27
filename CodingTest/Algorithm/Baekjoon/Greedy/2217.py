import sys
sys.stdin = open('input.txt')

N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort(reverse=True) # 가장 가벼운 중량을 들 수 있는 로프를 기준으로 오름차순 정렬

# 무게 15를 들으려면 15인 로프만 가능
# 10를 들으려면 10과 15 두 개의 로프 모두 가능하므로 10x2 = 20
# 최대로 들 수 있는 중량을 구하면되므로 list안에 추가하고 max로 출력

res_list = []
for i in range(N):
    res_list.append(rope[i] * (i+1))

print(max(res_list))