arr1 = []
arr2 = []
arr3 = []
n = int(input())
while len(arr1) <= n:
    arr1 = [int(x) for x in input().split()]
    break
while len(arr2) <= n:
    arr2 = [int(x) for x in input().split()]
    break
for i in range(n):
    arr3.append(arr1[i] + arr2[i])
print(' '.join(map(str, arr3)))