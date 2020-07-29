n, l = [int(x) for x in input().split()]
red = []
for i in range(n):
    red.append([int(i) for i in input().split()])
wx = 0
wy = 0
while wy<l:
    a = False
    for i in red:
        a = False
        if i[0] ==wy:
            if i[1]>wx%(i[1]+i[2]):
                wx += i[1]-wx%(i[1]+i[2])
            else:
                a =True
    if a:
        wx+=1
    wy+=1
print(wx+1)
