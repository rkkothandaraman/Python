count=0
x=int(input())
y=int(input())
li=[int(m) for m in input().split()]
for p in li:
    if p == y:
        count=count+1
print(count)