import sys
sys.stdin = open('input.txt')

def find_parents(x, parents):
    if x == parents[x]:
        return x
    else:
        return find_parents(parents[x], parents)

def union_parents(a,b,parents):
    a = find_parents(a, parents)
    b = find_parents(b, parents)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b
        
for T in range(int(input())):
    result = 0
    N, M = map(int, input().split())
    parents = [i for i in range(N)]

    data = tuple(map(int, input().split()))
    for i in range(len(data)//2):
        a = data[i*2]-1
        b = data[i*2+1]-1
        union_parents(a, b, parents)
    
    answer = []
    for a in parents:
        temp = find_parents(a, parents)
        if temp not in answer:
            answer.append(temp)
    
    print('#{} {}'.format((T+1), len(answer)))

#1 3
#2 2
#3 3