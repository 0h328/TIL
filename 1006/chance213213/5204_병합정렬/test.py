N = 5
list3 = [[0]*N for _ in range(N)]
list3[1] = 1
print(list3)

print(list3)
list1 = [1]
list1.insert(0, 2)
print(list1)


list2 = [1,2,3,4,5]
print(list2[-6])
print(list2[:-1])


for i in range(n):
    if not visited[i][col]:
        for j in range(n):
            visited[j][i] = 1
