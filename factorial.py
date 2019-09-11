N=int(input())
Fact=1
if(N and N<=20):
    for i in range(N,1,-1):
        Fact=Fact*i
    print(Fact)