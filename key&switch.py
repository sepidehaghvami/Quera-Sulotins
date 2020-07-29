n = int(input())
a = [input() for i in range(n)]
b = ''.join(a)
n = b.count('01')+b.count('10')
print(n)
