N,K=map(int,input().split())
li=[int(x) for x in input().split()]
if(N==len(li)):
    if K in li:
      print("yes")
    else:
        print("no")
