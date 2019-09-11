x,y,z=map(int,input().split())
if((x and y and z)and(x<=100000 and y<=100000 and z<=100000)):
    if((x+y>=z or y+z>=x or x+z>=y) and (x!=y!=z)):
        print("Yes")
    
