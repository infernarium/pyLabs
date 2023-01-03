import sys

maximal = 0
arr = []
n = int(input())

if n > 1000:
    print()
    exit()

for i in range(n):
    p = int(input())
    if p > maximal:
        maximal = p
print(str(maximal))

print (arr)
for line in sys.stdin:
    arr.append(int(line))
print(arr)
    
s = 0
for i in arr:
    if i == maximal:
        print(s)
    s +=1
