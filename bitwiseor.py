N=int(input())
li=[int(m) for m in input().split()]
if(N==len(li)):
    c=li[0]
    for i in range(len(li)):
        c = c|li[i]
    print (c)
