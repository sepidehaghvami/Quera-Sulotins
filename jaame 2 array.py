n, m = map(int, input().split())
a = []
b = []
c = [[0] * m for i in range(n)]
row1 = [] * m
row2 = [] * m

for i in range(n):
    row1 = list(map(int, input().split()))
    a.append(row1)

for j in range(n):
    row2 = list(map(int, input().split()))
    b.append(row2)

for i in range(n):
    for j in range(m):
        c[i][j]=a[i][j]+b[i][j]

for row in c:
    for elem in row:
        print(elem, end=' ')
    print()
print(len(a))