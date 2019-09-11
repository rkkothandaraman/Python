x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
x4,y4=map(int,input().split())
if (y2-y1==x3-x2==y3-y4==x4-x1):
    print ("yes")
else:
    print ("no")