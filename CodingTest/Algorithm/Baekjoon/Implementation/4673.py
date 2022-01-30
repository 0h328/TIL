self = set(range(1,10001))
not_self = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    not_self.add(i)

self = self - not_self

for i in sorted(self):
    print(i)