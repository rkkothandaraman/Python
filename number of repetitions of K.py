count=0
N,K=map(int,input().split())
li=[int(m) for m in input().split()]
if(len(li)==N):
    for p in li:
        if p == K:
            count=count+1
    print(count)