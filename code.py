n , t = input().split()
a = [input() for i in range(int(n))]
t = set([i for i in t])

for code in a:
    b= set([i for i in code])
    if b ==t:
        print("Yes")
    else:
        print("No")





