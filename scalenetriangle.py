x,y,z=map(int,input().split())
if(x and y and z):
    if((x+y>=z or y+z>=x or x+z>=y) and (x!=y!=z)):
        print("Yes")
    else:
        print("No")
else:
    print("No")