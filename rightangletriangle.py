x,y,z=map(int,input().split())
x,y,z=sorted([x,y,z])
if(x>=100000 or y>=100000 or z>=100000):
    print("No")
elif(x and y and z):
    if((x+y>=z) and (x!=y!=z) and (x**2+y**2==z**2)):
        print("Yes")
    else:
        print("No")
else:
    print("No")