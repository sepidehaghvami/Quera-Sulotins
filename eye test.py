test = []
result = []
comp = []
n = int(input())
while len(test) <= n:
    test = [str(x).split() for x in input()]
    break
while len(result) <= n:
    result = [str(x).split() for x in input()]
    break
answer = 0
for i in range(0,n):
    if test[i] != result[i]:
        answer = answer + 1
print(answer)
