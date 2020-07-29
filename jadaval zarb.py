n = int(input())
for i in range(1, 1 + n):
    list1 = []
    for j in range(1, 1 + n):
        list1.append(str(i * j))
    print(' '.join(list1))
