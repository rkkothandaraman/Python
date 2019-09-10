N=int(input())
li=[]
li=[int(m) for m in input().split()]
if(len(li)==N):
    maxi=li.index(max(li))
    mini=li.index(min(li))
print(mini+1,maxi+1)