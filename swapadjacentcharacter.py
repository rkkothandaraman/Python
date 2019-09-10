N=int(input())
li=list(map(int,input().split()))
temp=0
if(len(li)==N):
    for i in range(0,N-1,2):
        temp=li[i+1]
        li[i+1]=li[i]
        li[i]=temp
    for i in range(N):
        print(li[i], end=" ")
