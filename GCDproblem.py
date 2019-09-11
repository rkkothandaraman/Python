N,M=map(int,input().split())
GCD=1
li1=[]
li2=[]
li3=[]
if(N != 0 and M !=0):
    for i in range(1,N+1):
        if(N%i==0):
            li1.append(i)
    for j in range(1,M+1):
        if(M%j==0):
            li2.append(j)
    li3=set(li1)&set(li2)
    for i in li3:
        GCD=GCD*i
    print(GCD)
else:
	print('-1')
