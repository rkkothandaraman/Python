s=input()
N=len(s)
li=list(s)
temp=0
if(len(s)<=100000):
    for i in range(0,N,2):
        temp=li[i+1]
        li[i+1]=li[i]
        li[i]=temp
    print("".join(li))
